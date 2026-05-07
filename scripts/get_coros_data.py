#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
# ]
# ///
"""
从高驰 COROS 获取跑步数据并生成 running.json
包含 VDOT 跑力和训练负荷计算
"""

import argparse
import hashlib
import json
import logging
import math
import os
import sys
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

import httpx

# 心率区间配置
MAX_HR = int(os.environ.get("MAX_HR", 190))
RESTING_HR = int(os.environ.get("RESTING_HR", 55))

# 配置日志
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

COROS_URL_DICT = {
    "LOGIN_URL": "https://teamcnapi.coros.com/account/login",
    "ACTIVITY_LIST": "https://teamcnapi.coros.com/activity/query",
}

# 本地时区（UTC+8），COROS API 返回 UTC 时间戳，需统一转换
LOCAL_TZ = timezone(timedelta(hours=8))

TIME_OUT = httpx.Timeout(240.0, connect=360.0)

HEADERS = {
    "authority": "teamcnapi.coros.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json;charset=UTF-8",
    "dnt": "1",
    "origin": "https://t.coros.com",
    "referer": "https://t.coros.com/",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}


class VDOTCalculator:
    """
    VDOT 跑力计算器
    基于 Jack Daniels' Running Formula
    """

    def __init__(self, max_hr: int = MAX_HR, resting_hr: int = RESTING_HR):
        self.max_hr = max_hr
        self.resting_hr = resting_hr
        self.hr_reserve = max_hr - resting_hr

    def get_hr_zone(self, avg_hr: float) -> int:
        """根据最大心率百分比获取心率区间 (1-5)"""
        if avg_hr <= 0:
            return 0

        hr_percent = (avg_hr / self.max_hr) * 100

        if hr_percent < 70:
            return 1
        elif hr_percent < 80:
            return 2
        elif hr_percent < 87:
            return 3
        elif hr_percent < 93:
            return 4
        else:
            return 5

    def calculate_vdot(
        self,
        distance_meters: float,
        duration_seconds: float,
        avg_hr: Optional[float] = None,
    ) -> Optional[float]:
        """使用 Daniels Running Formula 计算 VDOT"""
        if duration_seconds <= 0 or distance_meters <= 0:
            return None

        duration_minutes = duration_seconds / 60
        velocity_m_per_min = distance_meters / duration_minutes

        if velocity_m_per_min <= 0:
            return None

        vo2 = -4.60 + 0.182258 * velocity_m_per_min + 0.000104 * (velocity_m_per_min**2)

        t = duration_minutes
        percent_vo2max = (
            0.8
            + 0.1894393 * math.exp(-0.012778 * t)
            + 0.2989558 * math.exp(-0.1932605 * t)
        )

        if percent_vo2max <= 0 or percent_vo2max > 1.0:
            return None

        vdot = vo2 / percent_vo2max

        if avg_hr and avg_hr > 0:
            hr_zone = self.get_hr_zone(avg_hr)
            zone_multipliers = {
                1: 0.97,
                2: 0.99,
                3: 1.00,
                4: 1.00,
                5: 1.00,
            }
            multiplier = zone_multipliers.get(hr_zone, 1.0)
            vdot *= multiplier

        if vdot < 20 or vdot > 100:
            return None

        return round(vdot, 1)

    def calculate_training_load(
        self, duration_seconds: float, avg_hr: Optional[float] = None
    ) -> int:
        """计算训练负荷"""
        if duration_seconds <= 0:
            return 0

        duration_hours = duration_seconds / 3600
        base_load = duration_hours * 100

        if avg_hr and avg_hr > 0:
            hr_zone = self.get_hr_zone(avg_hr)
            zone_factors = {
                1: 0.6,
                2: 0.8,
                3: 1.0,
                4: 1.3,
                5: 1.5,
            }
            factor = zone_factors.get(hr_zone, 1.0)
            base_load *= factor

        return round(base_load)


class CorosDataFetcher:
    """高驰 COROS 数据获取器"""

    RUNNING_SPORT_TYPES = {100, 101}  # 高驰跑步 sportType: 100=室外跑步, 101=室内跑步/跑步机

    def __init__(self, account: str, password: str):
        self.account = account
        self.password = password
        self.access_token: Optional[str] = None
        self.user_id: Optional[str] = None
        self.vdot_calculator = VDOTCalculator()

    def login(self) -> bool:
        """登录高驰，获取 accessToken"""
        try:
            encrypted_pwd = hashlib.md5(self.password.encode()).hexdigest()
            data = {
                "account": self.account,
                "accountType": 2,
                "pwd": encrypted_pwd,
            }

            resp = httpx.post(
                COROS_URL_DICT["LOGIN_URL"],
                json=data,
                headers=HEADERS,
                timeout=TIME_OUT,
            )
            resp.raise_for_status()
            result = resp.json()

            self.access_token = result.get("data", {}).get("accessToken")
            self.user_id = result.get("data", {}).get("userId")

            if not self.access_token:
                logger.error("登录失败，请检查账号和密码")
                return False

            logger.info("成功登录高驰 COROS")
            return True
        except Exception as e:
            logger.error(f"登录失败: {e}")
            return False

    def _get_auth_headers(self) -> Dict[str, str]:
        """获取带认证信息的请求头"""
        return {
            **HEADERS,
            "accesstoken": self.access_token or "",
            "cookie": f"CPL-coros-region=2; CPL-coros-token={self.access_token}",
        }

    def fetch_activities(
        self, page_number: int = 1, page_size: int = 50
    ) -> List[Dict[str, Any]]:
        """获取指定页码的活动列表"""
        url = (
            f"{COROS_URL_DICT['ACTIVITY_LIST']}"
            f"?modeList=&pageNumber={page_number}&size={page_size}"
        )

        resp = httpx.get(url, headers=self._get_auth_headers(), timeout=TIME_OUT)
        resp.raise_for_status()
        result = resp.json()

        activities = result.get("data", {}).get("dataList", [])
        return activities

    def get_all_activities(self) -> List[Dict[str, Any]]:
        """获取所有活动（自动分页）"""
        all_activities: List[Dict[str, Any]] = []
        page_number = 1
        page_size = 50

        while True:
            activities = self.fetch_activities(page_number, page_size)
            if not activities:
                break

            all_activities.extend(activities)
            logger.info(f"获取第 {page_number} 页，本页 {len(activities)} 条活动")

            # 如果本页不足 page_size 条，说明已到最后一页
            if len(activities) < page_size:
                break

            page_number += 1

        logger.info(f"共获取 {len(all_activities)} 条活动记录")
        return all_activities

    def get_activities_by_date(
        self, start_date: datetime, end_date: datetime
    ) -> List[Dict[str, Any]]:
        """获取指定日期范围内的活动（客户端过滤）"""
        all_activities = self.get_all_activities()
        filtered = []

        # 确保传入的日期带有时区信息（兼容 naive 和 aware datetime）
        if start_date.tzinfo is None:
            start_date = start_date.replace(tzinfo=LOCAL_TZ)
        if end_date.tzinfo is None:
            end_date = end_date.replace(tzinfo=LOCAL_TZ)

        for activity in all_activities:
            start_time = activity.get("startTime", 0)
            if start_time:
                activity_dt = datetime.fromtimestamp(start_time, tz=LOCAL_TZ)
                if start_date <= activity_dt <= end_date:
                    filtered.append(activity)

        logger.info(
            f"日期过滤后剩余 {len(filtered)} 条活动 ({start_date.date()} ~ {end_date.date()})"
        )
        return filtered

    def filter_running_activities(
        self, activities: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """过滤出跑步活动"""
        running_activities = []

        for activity in activities:
            sport_type = activity.get("sportType")
            if sport_type in self.RUNNING_SPORT_TYPES:
                running_activities.append(activity)
                logger.info(
                    f"找到跑步活动: {self._format_timestamp(activity.get('startTime', 0))}"
                    f" - {activity.get('name', '未知')}"
                    f" ({self._get_activity_type(activity)})"
                )

        logger.info(f"过滤出 {len(running_activities)} 个跑步活动")
        return running_activities

    def _get_activity_type(self, activity: Dict[str, Any]) -> str:
        """获取跑步活动类型"""
        sub_mode = activity.get("subMode", 0)
        if sub_mode == 2:
            return "跑步机"
        return "室外跑步"

    def _format_timestamp(self, timestamp: int) -> str:
        """将 Unix 时间戳格式化为日期时间字符串（UTC+8）"""
        if not timestamp:
            return ""
        return datetime.fromtimestamp(timestamp, tz=LOCAL_TZ).strftime("%Y-%m-%d %H:%M:%S")

    def _seconds_to_pace(self, pace_seconds: float) -> str:
        """将秒/公里转换为配速字符串"""
        if pace_seconds <= 0:
            return "0'00\""
        minutes = int(pace_seconds // 60)
        seconds = int(pace_seconds % 60)
        return f"{minutes}'{seconds:02d}\""

    def _seconds_to_duration(self, total_seconds: int) -> str:
        """将秒数转换为时长字符串"""
        if total_seconds <= 0:
            return "0分钟"

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        if hours > 0:
            return f"{hours}小时{minutes}分钟"
        return f"{minutes}分钟"

    def format_running_data(
        self, activities: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """格式化跑步数据为 running.json 所需格式"""
        stats = {
            "total_runs": len(activities),
            "total_distance": 0,
            "total_duration": "0小时0分钟",
            "avg_pace": "0'00\"",
            "longest_run": 0,
            "avg_vdot": 0,
            "total_training_load": 0,
        }

        total_seconds = 0
        total_vdot = 0
        vdot_count = 0
        formatted_runs = []

        for activity in activities:
            distance = activity.get("distance", 0) / 1000  # km
            distance_meters = activity.get("distance", 0)
            duration_seconds = activity.get("totalTime", 0)
            avg_hr = activity.get("avgHr", 0)
            max_hr = activity.get("maxHr", 0) or 0
            cadence = activity.get("avgCadence", 0) or activity.get("cadence", 0) or 0
            avg_power = activity.get("avgPower", 0) or 0
            max_power = activity.get("maxPower", 0) or 0
            calories_raw = activity.get("calorie", 0) or 0
            calories = round(calories_raw / 1000) if calories_raw else 0
            elevation_gain = activity.get("ascent", 0) or 0
            avg_speed = activity.get("avgSpeed", 0)  # 秒/公里
            pace = self._seconds_to_pace(avg_speed)
            device = activity.get("device", "")

            # 计算 VDOT 和训练负荷
            vdot = self.vdot_calculator.calculate_vdot(
                distance_meters, duration_seconds, avg_hr
            )
            training_load = self.vdot_calculator.calculate_training_load(
                duration_seconds, avg_hr
            )

            # 更新统计数据
            stats["total_distance"] += distance
            stats["longest_run"] = max(stats["longest_run"], distance)
            stats["total_training_load"] += training_load
            total_seconds += duration_seconds

            if vdot:
                total_vdot += vdot
                vdot_count += 1

            # 获取心率区间
            hr_zone = self.vdot_calculator.get_hr_zone(avg_hr) if avg_hr > 0 else 0

            run_data = {
                "date": self._format_timestamp(activity.get("startTime", 0)),
                "distance": round(distance, 2),
                "duration": self._seconds_to_duration(duration_seconds),
                "pace": pace,
                "heart_rate": round(avg_hr, 1) if avg_hr else 0,
                "max_heart_rate": round(max_hr, 1) if max_hr else 0,
                "cadence": round(cadence) if cadence else 0,
                "stride_length": 0,  # 高驰 API 列表中不提供步幅
                "avg_power": round(avg_power) if avg_power else 0,
                "max_power": round(max_power) if max_power else 0,
                "calories": calories,
                "elevation_gain": round(elevation_gain, 1) if elevation_gain else 0,
                "route": "未知路线",
                "weather": "未知天气",
                "activity_type": self._get_activity_type(activity),
                "workout_name": activity.get("name", ""),
                "vdot": vdot,
                "training_load": training_load,
                "hr_zone": hr_zone,
            }

            formatted_runs.append(run_data)

        # 计算平均配速
        if stats["total_distance"] > 0:
            avg_pace_seconds = total_seconds / stats["total_distance"]
            stats["avg_pace"] = self._seconds_to_pace(avg_pace_seconds)

        # 计算平均 VDOT
        if vdot_count > 0:
            stats["avg_vdot"] = round(total_vdot / vdot_count, 1)

        # 格式化总持续时间
        stats["total_duration"] = self._seconds_to_duration(total_seconds)

        # 保留一位小数
        stats["total_distance"] = round(stats["total_distance"], 1)
        stats["longest_run"] = round(stats["longest_run"], 1)

        # 按日期排序（最新的在前）
        formatted_runs.sort(key=lambda x: x["date"], reverse=True)

        return {
            "stats": stats,
            "runs": formatted_runs,
        }

    def save_to_hugo_data(
        self, data: Dict[str, Any], output_path: str = "data/running.json", merge: bool = True
    ) -> bool:
        """保存数据到 running.json"""
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            if merge and os.path.exists(output_path):
                try:
                    with open(output_path, "r", encoding="utf-8") as f:
                        existing_data = json.load(f)

                    merged_data = self._merge_running_data(existing_data, data)
                    data = merged_data
                    logger.info(f"已与现有数据合并，共 {len(data['runs'])} 条跑步记录")
                except Exception as e:
                    logger.warning(f"合并现有数据失败，将覆盖文件: {e}")

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            logger.info(f"数据已保存到 {output_path}")
            return True
        except Exception as e:
            logger.error(f"保存数据失败: {e}")
            return False

    def _is_same_run(self, run_a: Dict[str, Any], run_b: Dict[str, Any]) -> bool:
        """
        判断两条记录是否是同一次跑步

        判断规则：
        1. 精确匹配 date（包含时间）
        2. 或同一天 + 同距离 + 同时长（容错不同数据源时间戳差几秒的情况）
        """
        # 1. 精确匹配 date
        if run_a.get("date") == run_b.get("date"):
            return True

        # 2. 同一天 + 同距离 + 同时长
        date_a = run_a.get("date", "").split(" ")[0]
        date_b = run_b.get("date", "").split(" ")[0]
        if date_a and date_a == date_b:
            distance_a = run_a.get("distance", 0)
            distance_b = run_b.get("distance", 0)
            duration_a = run_a.get("duration", "")
            duration_b = run_b.get("duration", "")
            if (distance_a == distance_b and
                duration_a == duration_b and
                distance_a is not None and distance_a > 0):
                return True

        return False

    def _deduplicate_runs(self, runs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """对跑步记录列表进行去重"""
        unique_runs: List[Dict[str, Any]] = []
        for run in runs:
            is_duplicate = False
            for existing in unique_runs:
                if self._is_same_run(existing, run):
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_runs.append(run)
        return unique_runs

    def _merge_running_data(
        self, existing_data: Dict[str, Any], new_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """合并跑步数据（与 Garmin 脚本逻辑一致）"""
        existing_runs = existing_data.get("runs", [])

        # 先对现有数据去重（防止历史数据已存在重复）
        existing_runs = self._deduplicate_runs(existing_runs)

        for new_run in new_data.get("runs", []):
            matched = False
            for existing_run in existing_runs:
                if self._is_same_run(existing_run, new_run):
                    for key, value in new_run.items():
                        if key == "date":
                            pass
                        elif key not in existing_run:
                            existing_run[key] = value
                        elif key in ["segments", "laps"]:
                            if value and len(value) > 0:
                                existing_run[key] = value
                        else:
                            if value and value != 0 and value != "0'00\"":
                                existing_run[key] = value
                    matched = True
                    break

            if not matched:
                existing_runs.append(new_run)

        # 最终去重（防止新数据内部或合并后产生重复）
        existing_runs = self._deduplicate_runs(existing_runs)

        existing_data["runs"] = existing_runs
        existing_data["runs"].sort(key=lambda x: x["date"], reverse=True)
        existing_data["stats"] = self._recalculate_stats(existing_data["runs"])

        return existing_data

    def _recalculate_stats(self, runs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """重新计算统计数据"""
        stats = {
            "total_runs": len(runs),
            "total_distance": 0,
            "total_duration": "0小时0分钟",
            "avg_pace": "0'00\"",
            "longest_run": 0,
            "avg_vdot": 0,
            "total_training_load": 0,
            "period_stats": {},
        }

        total_seconds = 0
        total_vdot = 0
        vdot_count = 0

        for run in runs:
            distance = run["distance"]
            duration_str = run["duration"]

            stats["total_distance"] += distance
            stats["longest_run"] = max(stats["longest_run"], distance)

            if "training_load" in run:
                stats["total_training_load"] += run["training_load"]

            if "vdot" in run and run["vdot"]:
                total_vdot += run["vdot"]
                vdot_count += 1

            # 解析持续时间字符串
            duration_parts = duration_str.replace("小时", ":").replace("分钟", "").split(":")
            if len(duration_parts) == 2:
                hours = int(duration_parts[0])
                minutes = int(duration_parts[1])
                total_seconds += hours * 3600 + minutes * 60
            else:
                minutes = int(duration_parts[0])
                total_seconds += minutes * 60

        # 计算平均配速
        if stats["total_distance"] > 0:
            avg_pace_seconds = total_seconds / stats["total_distance"]
            stats["avg_pace"] = self._seconds_to_pace(avg_pace_seconds)

        # 计算平均 VDOT
        if vdot_count > 0:
            stats["avg_vdot"] = round(total_vdot / vdot_count, 1)

        # 格式化总持续时间
        stats["total_duration"] = self._seconds_to_duration(total_seconds)

        # 保留一位小数
        stats["total_distance"] = round(stats["total_distance"], 1)
        stats["longest_run"] = round(stats["longest_run"], 1)

        # 计算各周期统计
        stats["period_stats"] = self._calculate_period_stats(runs)

        return stats

    def _calculate_period_stats(
        self, runs: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """计算各周期（周、月、年、总）的统计数据"""
        now = datetime.now()

        period_ranges = {
            "week": {
                "start": now - timedelta(days=7),
                "end": now,
            },
            "month": {
                "start": datetime(now.year, now.month, 1),
                "end": now,
            },
            "year": {
                "start": datetime(now.year, 1, 1),
                "end": now,
            },
            "total": {
                "start": datetime.min,
                "end": now,
            },
        }

        period_stats = {}

        for period_name, date_range in period_ranges.items():
            period_data = self._calculate_stats_for_period(
                runs, date_range["start"], date_range["end"]
            )
            period_stats[period_name] = period_data

        return period_stats

    def _calculate_stats_for_period(
        self, runs: List[Dict[str, Any]], start_date: datetime, end_date: datetime
    ) -> Dict[str, Any]:
        """计算指定周期内的统计数据"""
        period_runs = []
        for run in runs:
            try:
                run_date = datetime.strptime(run["date"].split(" ")[0], "%Y-%m-%d")
                if start_date <= run_date <= end_date:
                    period_runs.append(run)
            except (ValueError, IndexError):
                continue

        if not period_runs:
            return {
                "total_activities": 0,
                "total_distance": 0,
                "total_duration_hours": 0,
                "avg_pace": "--",
                "avg_heart_rate": None,
                "avg_vdot": None,
                "total_training_load": 0,
            }

        total_distance = sum(r["distance"] for r in period_runs)
        total_activities = len(period_runs)
        total_training_load = sum(r.get("training_load", 0) for r in period_runs)

        total_seconds = 0
        total_hr = 0
        hr_count = 0
        total_vdot = 0
        vdot_count = 0

        for run in period_runs:
            duration_str = run["duration"]
            duration_parts = duration_str.replace("小时", ":").replace("分钟", "").split(":")
            if len(duration_parts) == 2:
                hours = int(duration_parts[0])
                minutes = int(duration_parts[1])
                total_seconds += hours * 3600 + minutes * 60
            else:
                minutes = int(duration_parts[0])
                total_seconds += minutes * 60

            hr = run.get("heart_rate", 0)
            if hr and hr > 0:
                total_hr += hr
                hr_count += 1

            vdot = run.get("vdot")
            if vdot and vdot > 0:
                total_vdot += vdot
                vdot_count += 1

        avg_pace = "--"
        if total_distance > 0:
            avg_pace_seconds = total_seconds / total_distance
            avg_pace = self._seconds_to_pace(avg_pace_seconds)

        avg_hr = round(total_hr / hr_count) if hr_count > 0 else None
        avg_vdot = round(total_vdot / vdot_count, 1) if vdot_count > 0 else None
        total_hours = round(total_seconds / 3600, 1)

        return {
            "total_activities": total_activities,
            "total_distance": round(total_distance, 1),
            "total_duration_hours": total_hours,
            "avg_pace": avg_pace,
            "avg_heart_rate": avg_hr,
            "avg_vdot": avg_vdot,
            "total_training_load": total_training_load,
        }


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="从高驰 COROS 获取跑步数据")

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--days", type=int, default=30, help="获取最近多少天的跑步数据 (默认: 30)"
    )
    group.add_argument("--year", type=int, help="获取指定年份的跑步数据")
    group.add_argument("--all", action="store_true", help="获取所有跑步数据")

    parser.add_argument(
        "--output",
        type=str,
        default="src/data/running.json",
        help="输出文件路径 (默认: src/data/running.json)",
    )
    parser.add_argument(
        "--no-merge", action="store_true", help="不与现有数据合并，直接覆盖文件"
    )
    parser.add_argument(
        "--account",
        type=str,
        help="高驰账号 (也可通过环境变量 COROS_ACCOUNT 设置)",
    )
    parser.add_argument(
        "--password",
        type=str,
        help="高驰密码 (也可通过环境变量 COROS_PASSWORD 设置)",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    account = args.account or os.environ.get("COROS_ACCOUNT", "")
    password = args.password or os.environ.get("COROS_PASSWORD", "")

    if not account or not password:
        print("请设置环境变量 COROS_ACCOUNT 和 COROS_PASSWORD")
        print("或者使用 --account 和 --password 参数")
        sys.exit(1)

    fetcher = CorosDataFetcher(account, password)

    if not fetcher.login():
        print("登录失败，请检查账号和密码")
        return

    activities = []

    now = datetime.now(LOCAL_TZ)

    if args.all:
        print("获取所有跑步数据...")
        activities = fetcher.get_all_activities()
    elif args.year:
        print(f"获取 {args.year} 年的跑步数据...")
        if args.year == now.year:
            start_date = datetime(args.year, 1, 1, tzinfo=LOCAL_TZ)
            end_date = now
        else:
            start_date = datetime(args.year, 1, 1, tzinfo=LOCAL_TZ)
            end_date = datetime(args.year, 12, 31, 23, 59, 59, tzinfo=LOCAL_TZ)

        activities = fetcher.get_activities_by_date(start_date, end_date)
    else:
        print(f"获取最近 {args.days} 天的跑步数据...")
        end_date = now
        start_date = end_date - timedelta(days=args.days)
        activities = fetcher.get_activities_by_date(start_date, end_date)

    # 过滤跑步活动
    running_activities = fetcher.filter_running_activities(activities)

    if not running_activities:
        print("没有找到跑步活动")
        return

    # 格式化数据
    running_data = fetcher.format_running_data(running_activities)

    # 保存到数据文件
    merge = not args.no_merge
    if fetcher.save_to_hugo_data(running_data, args.output, merge):
        print("跑步数据获取并保存成功！")

        # 打印统计信息
        stats = running_data["stats"]
        print(f"\n本次获取的跑步统计:")
        print(f"跑步次数: {stats['total_runs']}")
        print(f"跑步距离: {stats['total_distance']} 公里")
        print(f"跑步时间: {stats['total_duration']}")
        print(f"平均配速: {stats['avg_pace']}")
        print(f"最长距离: {stats['longest_run']} 公里")
        if stats.get("avg_vdot"):
            print(f"平均 VDOT: {stats['avg_vdot']}")
        if stats.get("total_training_load"):
            print(f"总训练负荷: {stats['total_training_load']}")

        print(f"\n前5条跑步记录:")
        for i, run in enumerate(running_data["runs"][:5]):
            workout_info = (
                f" [{run.get('workout_name', '')}]" if run.get("workout_name") else ""
            )
            vdot_info = f" VDOT:{run['vdot']}" if run.get("vdot") else ""
            load_info = f" 负荷:{run['training_load']}" if run.get("training_load") else ""
            print(
                f"  {i+1}. {run['date']}: {run['distance']}km, {run['pace']}/km{workout_info}{vdot_info}{load_info}"
            )

        # 如果是合并模式，打印总统计信息
        if merge and os.path.exists(args.output):
            try:
                with open(args.output, "r", encoding="utf-8") as f:
                    total_data = json.load(f)
                total_stats = total_data["stats"]
                print(f"\n总跑步统计:")
                print(f"总跑步次数: {total_stats['total_runs']}")
                print(f"总跑步距离: {total_stats['total_distance']} 公里")
                print(f"总跑步时间: {total_stats['total_duration']}")
                print(f"平均配速: {total_stats['avg_pace']}")
                print(f"最长距离: {total_stats['longest_run']} 公里")
                if total_stats.get("avg_vdot"):
                    print(f"平均 VDOT: {total_stats['avg_vdot']}")
                if total_stats.get("total_training_load"):
                    print(f"总训练负荷: {total_stats['total_training_load']}")
            except Exception as e:
                logger.warning(f"读取总统计数据失败: {e}")
    else:
        print("保存数据失败")


if __name__ == "__main__":
    main()
