#!/usr/bin/env python3
# /// script
# dependencies = [
#   "garminconnect>=0.1.20",
#   "python-dotenv>=0.19.0",
# ]
# ///
"""
使用 garminconnect 获取跑步数据并生成 Hugo 数据文件
包含 VDOT 跑力和训练负荷计算
"""

import json
import logging
import math
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import os
import sys
import argparse

# 心率区间配置
MAX_HR = int(os.environ.get('MAX_HR', 190))  # 最大心率
RESTING_HR = int(os.environ.get('RESTING_HR', 55))  # 静息心率
HR_RESERVE = MAX_HR - RESTING_HR  # 心率储备

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from garminconnect import Garmin
except ImportError:
    print("请先安装 garminconnect: uv run get_garmin_data.py")
    sys.exit(1)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
            return 1  # Zone 1: <70% (轻松跑)
        elif hr_percent < 80:
            return 2  # Zone 2: 70-80% (有氧基础)
        elif hr_percent < 87:
            return 3  # Zone 3: 80-87% (节奏跑)
        elif hr_percent < 93:
            return 4  # Zone 4: 87-93% (乳酸阈)
        else:
            return 5  # Zone 5: >93% (最大摄氧量)
    
    def calculate_vdot(self, distance_meters: float, duration_seconds: float, avg_hr: Optional[float] = None) -> Optional[float]:
        """
        使用 Daniels Running Formula 计算 VDOT
        
        Args:
            distance_meters: 距离（米）
            duration_seconds: 时长（秒）
            avg_hr: 平均心率（可选）
        
        Returns:
            VDOT 值，如果计算失败返回 None
        """
        if duration_seconds <= 0 or distance_meters <= 0:
            return None
        
        # 转换为分钟
        duration_minutes = duration_seconds / 60
        
        # 速度（米/分钟）
        velocity_m_per_min = distance_meters / duration_minutes
        
        if velocity_m_per_min <= 0:
            return None
        
        # 计算 VO2（Daniels 公式）
        # VO2 = -4.60 + 0.182258 * v + 0.000104 * v²
        vo2 = -4.60 + 0.182258 * velocity_m_per_min + 0.000104 * (velocity_m_per_min ** 2)
        
        # 根据时长计算 %VO2max
        # %VO2max = 0.8 + 0.1894393 * e^(-0.012778*t) + 0.2989558 * e^(-0.1932605*t)
        t = duration_minutes
        percent_vo2max = (0.8
                        + 0.1894393 * math.exp(-0.012778 * t)
                        + 0.2989558 * math.exp(-0.1932605 * t))
        
        if percent_vo2max <= 0 or percent_vo2max > 1.0:
            return None
        
        # 计算基础 VDOT
        vdot = vo2 / percent_vo2max
        
        # 根据心率区间微调
        if avg_hr and avg_hr > 0:
            hr_zone = self.get_hr_zone(avg_hr)
            
            # 心率效率调整系数
            zone_multipliers = {
                1: 0.97,  # 轻松跑
                2: 0.99,  # 有氧基础
                3: 1.00,  # 节奏跑
                4: 1.00,  # 乳酸阈
                5: 1.00   # 最大摄氧量
            }
            
            multiplier = zone_multipliers.get(hr_zone, 1.0)
            vdot *= multiplier
        
        # VDOT 合理范围检查
        if vdot < 20 or vdot > 100:
            return None
        
        return round(vdot, 1)
    
    def calculate_training_load(self, duration_seconds: float, avg_hr: Optional[float] = None) -> int:
        """
        计算训练负荷
        
        Args:
            duration_seconds: 时长（秒）
            avg_hr: 平均心率（可选）
        
        Returns:
            训练负荷值
        """
        if duration_seconds <= 0:
            return 0
        
        duration_hours = duration_seconds / 3600
        
        # 基础负荷 = 时长(小时) * 100
        base_load = duration_hours * 100
        
        # 根据心率区间调整
        if avg_hr and avg_hr > 0:
            hr_zone = self.get_hr_zone(avg_hr)
            
            # 心率区间系数
            zone_factors = {
                1: 0.6,   # 轻松恢复
                2: 0.8,   # 有氧基础
                3: 1.0,   # 节奏跑
                4: 1.3,   # 乳酸阈
                5: 1.5    # 最大摄氧量
            }
            
            factor = zone_factors.get(hr_zone, 1.0)
            base_load *= factor
        
        return round(base_load)


class GarminDataFetcher:
    def __init__(self, email: str, password: str):
        """
        初始化 Garmin 数据获取器

        Args:
            email: Garmin 账户邮箱
            password: Garmin 账户密码
        """
        self.email = email
        self.password = password
        self.client = None
        self.vdot_calculator = VDOTCalculator()

    def login(self) -> bool:
        """登录 Garmin Connect"""
        try:
            self.client = Garmin(self.email, self.password)
            self.client.login()
            logger.info("成功登录 Garmin Connect")
            return True
        except Exception as e:
            logger.error(f"登录失败: {e}")
            return False

    def get_activities(self, days: int = 30) -> List[Dict[str, Any]]:
        """
        获取指定天数内的活动数据

        Args:
            days: 获取最近多少天的数据

        Returns:
            活动数据列表
        """
        if not self.client:
            logger.error("请先登录")
            return []

        try:
            # 获取活动数据
            activities = self.client.get_activities_by_date(
                (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d"),
                datetime.now().strftime("%Y-%m-%d")
            )
            logger.info(f"获取到 {len(activities)} 个活动")
            return activities
        except Exception as e:
            logger.error(f"获取活动数据失败: {e}")
            return []

    def get_activities_by_date(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        """
        获取指定日期范围内的活动数据

        Args:
            start_date: 开始日期 (YYYY-MM-DD)
            end_date: 结束日期 (YYYY-MM-DD)

        Returns:
            活动数据列表
        """
        if not self.client:
            logger.error("请先登录")
            return []

        try:
            # 获取指定日期范围内的活动数据
            activities = self.client.get_activities_by_date(start_date, end_date)
            logger.info(f"获取到 {len(activities)} 个活动")
            return activities
        except Exception as e:
            logger.error(f"获取活动数据失败: {e}")
            return []

    def _print_activity_details(self, activity: Dict[str, Any], index: int = 0):
        """
        打印活动的详细信息（用于调试）

        Args:
            activity: 活动数据
            index: 活动索引
        """
        logger.info(f"\n{'='*60}")
        logger.info(f"活动 {index} 的完整数据结构:")
        logger.info(f"{'='*60}")
        
        # 打印所有顶层字段
        logger.info("顶层字段:")
        for key in sorted(activity.keys()):
            value = activity[key]
            if isinstance(value, (dict, list)):
                logger.info(f"  {key}: <{type(value).__name__}>")
            else:
                logger.info(f"  {key}: {value}")
        
        # 特别关注可能包含训练名称的字段
        logger.info("\n可能包含训练名称的字段:")
        name_fields = ['activityName', 'name', 'description', 'workoutName', 'courseName', 
                       'trainingPlanName', 'trainingType', 'sportType', 'subSportType',
                       'eventType', 'activityType', 'workout', 'training']
        for field in name_fields:
            if field in activity:
                logger.info(f"  {field}: {activity[field]}")
        
        # 详细查看 activityType
        if 'activityType' in activity:
            logger.info(f"\nactivityType 详情: {activity['activityType']}")
        
        # 查看是否有 workout 相关数据
        if 'workout' in activity:
            logger.info(f"\nworkout 详情: {activity['workout']}")
        
        logger.info(f"{'='*60}\n")

    def filter_running_activities(self, activities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        过滤出跑步活动

        Args:
            activities: 所有活动数据

        Returns:
            跑步活动数据列表
        """
        running_activities = []

        # 调试：打印第一个活动的完整数据结构
        if activities:
            logger.info("调试：打印第一个活动的完整数据结构")
            self._print_activity_details(activities[0], 1)
            
            # 也打印前3个活动的关键字段用于对比
            logger.info("\n前3个活动的关键字段对比:")
            for i, activity in enumerate(activities[:3]):
                activity_type = activity.get('activityType', {})
                type_key = activity_type.get('typeKey', 'unknown')
                display_name = activity_type.get('displayName', 'unknown')
                activity_name = activity.get('activityName', 'N/A')
                name = activity.get('name', 'N/A')
                description = activity.get('description', 'N/A')[:50] if activity.get('description') else 'N/A'
                workout = activity.get('workout', 'N/A')
                logger.info(f"活动 {i+1}: typeKey={type_key}, displayName={display_name}")
                logger.info(f"         activityName={activity_name}, name={name}")
                logger.info(f"         description={description}...")
                logger.info(f"         workout={workout}")

        # 尝试多种可能的跑步活动类型标识
        running_type_keys = ['running', 'run', 'jogging', 'trail_running', 'treadmill_running']
        running_display_names = ['跑步', 'Running', 'Run', 'Jogging', 'Trail Running', 'Treadmill Running']

        for activity in activities:
            activity_type = activity.get('activityType', {})
            type_key = activity_type.get('typeKey', '').lower()
            display_name = activity_type.get('displayName', '').lower()

            # 检查是否是跑步活动
            is_running = (
                type_key in running_type_keys or
                display_name in running_display_names or
                'run' in type_key or
                'running' in type_key or
                'run' in display_name or
                'running' in display_name or
                'treadmill' in type_key or
                'treadmill' in display_name
            )

            if is_running:
                running_activities.append(activity)
                activity_category = self._get_activity_type(activity)
                logger.info(f"找到跑步活动: {activity.get('startTimeLocal', '')} - {display_name} ({activity_category})")

        logger.info(f"过滤出 {len(running_activities)} 个跑步活动")
        return running_activities

    def _get_activity_type(self, activity: Dict[str, Any]) -> str:
        """
        获取跑步活动类型（室外跑步或跑步机）

        Args:
            activity: 活动数据

        Returns:
            活动类型字符串：'室外跑步', '跑步机', '未知'
        """
        activity_type = activity.get('activityType', {})
        type_key = activity_type.get('typeKey', '').lower()
        display_name = activity_type.get('displayName', '').lower()

        # 判断是否为跑步机
        if ('treadmill' in type_key or
            'treadmill' in display_name or
            '跑步机' in display_name or
            type_key == 'treadmill_running'):
            return '跑步机'

        # 判断是否为越野跑
        elif ('trail' in type_key or
              'trail' in display_name or
              '越野' in display_name or
              type_key == 'trail_running'):
            return '越野跑'

        # 判断是否为室外跑步（默认情况）
        elif (type_key in ['running', 'run', 'jogging'] or
              'running' in type_key or
              'run' in type_key or
              'jogging' in type_key or
              '跑步' in display_name):
            return '室外跑步'

        # 其他情况返回未知
        else:
            return '未知'

    def _get_workout_name(self, activity: Dict[str, Any]) -> str:
        """
        获取训练名称（如"轻松跑"、"间歇跑"等）

        Args:
            activity: 活动数据

        Returns:
            训练名称，如果没有则返回空字符串
        """
        # 尝试多个可能的字段
        # 1. activityName - 用户自定义的活动名称
        if activity.get('activityName'):
            return activity['activityName']
        
        # 2. name - 另一个可能的字段
        if activity.get('name'):
            return activity['name']
        
        # 3. workout 对象中的名称
        workout = activity.get('workout', {})
        if isinstance(workout, dict):
            workout_name = workout.get('workoutName') or workout.get('name')
            if workout_name:
                return workout_name
        
        # 4. trainingPlan 中的名称
        training_plan = activity.get('trainingPlan', {})
        if isinstance(training_plan, dict):
            plan_name = training_plan.get('trainingPlanName') or training_plan.get('name')
            if plan_name:
                return plan_name
        
        # 5. 从 description 中提取（有些用户会在描述中写训练类型）
        description = activity.get('description', '')
        if description:
            # 取第一行或前20个字符
            first_line = description.split('\n')[0][:30]
            return first_line
        
        return ''

    def _get_activity_details(self, activity_id: str) -> Dict[str, Any]:
        """
        获取活动的详细数据（分段、记圈等）
        
        Args:
            activity_id: 活动ID
            
        Returns:
            详细数据字典
        """
        details = {
            'segments': [],
            'laps': []
        }
        
        if not self.client or not activity_id:
            return details
            
        try:
            # 获取活动分段数据（splits）
            logger.info(f"获取活动 {activity_id} 的详细数据...")
            splits_data = self.client.get_activity_splits(activity_id)
            logger.debug(f"splits_data keys: {splits_data.keys() if splits_data else 'None'}")
            if splits_data and 'lapDTOs' in splits_data:
                laps = splits_data['lapDTOs']
                logger.info(f"活动 {activity_id}: 获取到 {len(laps)} 个 lapDTOs")
                
                # 处理记圈数据（laps）
                for lap in laps:
                    # 获取速度，尝试多个字段
                    speed = self._get_speed_from_lap(lap)
                    
                    # 如果找不到速度，通过距离和时间计算配速
                    if speed > 0:
                        pace = self._format_pace(speed)
                    else:
                        pace = self._calculate_pace_from_distance_time(
                            lap.get('distance', 0),
                            lap.get('duration', 0)
                        )
                    
                    # 获取功率，尝试多个可能的字段名
                    power = 0
                    for power_field in ['avgPower', 'averagePower', 'power', 'currentPower']:
                        power_val = lap.get(power_field, 0)
                        if power_val and power_val > 0:
                            power = round(power_val)
                            break
                    
                    # 获取步频，尝试多个可能的字段名
                    cadence = 0
                    for cadence_field in ['averageRunCadence', 'avgRunCadence', 'runCadence', 'cadence']:
                        cadence_val = lap.get(cadence_field, 0)
                        if cadence_val and cadence_val > 0:
                            cadence = round(cadence_val)
                            break
                    
                    lap_data = {
                        'distance': round(lap.get('distance', 0) / 1000, 2),  # km
                        'pace': pace,
                        'cadence': cadence,
                        'power': power,
                        'heart_rate': round(lap.get('averageHR', 0)),
                        'hr_zone': self.vdot_calculator.get_hr_zone(lap.get('averageHR', 0))
                    }
                    details['laps'].append(lap_data)
                
                # 从 lapDTOs 中提取分段数据（segments）
                # 通常每公里一个分段，根据 distance 字段判断
                segment_distance = 0
                current_segment_laps = []
                segment_number = 1
                
                for lap in laps:
                    lap_distance = lap.get('distance', 0) / 1000  # km
                    segment_distance += lap_distance
                    current_segment_laps.append(lap)
                    
                    # 当累计距离达到或超过1公里时，创建一个分段
                    if segment_distance >= 0.99:  # 允许小的误差
                        # 计算该分段的平均数据
                        avg_hr = sum(l.get('averageHR', 0) for l in current_segment_laps) / len(current_segment_laps) if current_segment_laps else 0
                        
                        # 计算该分段的总距离和总时间
                        total_distance_m = sum(l.get('distance', 0) for l in current_segment_laps)
                        total_duration_sec = sum(l.get('duration', 0) for l in current_segment_laps)
                        
                        # 通过距离和时间计算配速
                        pace = self._calculate_pace_from_distance_time(total_distance_m, total_duration_sec)
                        
                        segment_data = {
                            'km': segment_number,
                            'pace': pace,
                            'gap': pace,  # GAP 暂时用平均配速
                            'heart_rate': round(avg_hr) if avg_hr else 0,
                            'hr_zone': self.vdot_calculator.get_hr_zone(avg_hr)
                        }
                        details['segments'].append(segment_data)
                        
                        # 重置分段数据
                        segment_distance = 0
                        current_segment_laps = []
                        segment_number += 1
                
                # 处理剩余的距离（如果有）
                if current_segment_laps and segment_distance > 0.1:  # 至少100米才记录
                    avg_hr = sum(l.get('averageHR', 0) for l in current_segment_laps) / len(current_segment_laps) if current_segment_laps else 0
                    
                    # 计算剩余分段的总距离和总时间
                    total_distance_m = sum(l.get('distance', 0) for l in current_segment_laps)
                    total_duration_sec = sum(l.get('duration', 0) for l in current_segment_laps)
                    
                    # 通过距离和时间计算配速
                    pace = self._calculate_pace_from_distance_time(total_distance_m, total_duration_sec)
                    
                    segment_data = {
                        'km': round(segment_distance, 2),  # 显示实际距离，如 0.31
                        'pace': pace,
                        'gap': pace,
                        'heart_rate': round(avg_hr) if avg_hr else 0,
                        'hr_zone': self.vdot_calculator.get_hr_zone(avg_hr)
                    }
                    details['segments'].append(segment_data)
                    
        except Exception as e:
            logger.warning(f"获取活动 {activity_id} 详细数据失败: {e}")
            
        return details
    
    def _get_speed_from_lap(self, lap: Dict[str, Any]) -> float:
        """
        从 lap 数据中获取速度（米/秒）
        尝试多个可能的字段名
        
        Args:
            lap: lap 数据字典
            
        Returns:
            速度（米/秒），如果找不到则返回 0
        """
        # 尝试多个可能的字段名
        speed_fields = ['speed', 'averageSpeed', 'avgSpeed', 'currentSpeed']
        for field in speed_fields:
            speed = lap.get(field, 0)
            if speed and speed > 0:
                return speed
        
        # 如果找不到速度，尝试通过距离和时间计算
        distance = lap.get('distance', 0)  # 米
        duration = lap.get('duration', 0)  # 秒
        if distance > 0 and duration > 0:
            return distance / duration
        
        return 0
    
    def _format_pace(self, speed_m_per_s: float) -> str:
        """
        将速度（米/秒）转换为配速（分钟/公里）
        
        Args:
            speed_m_per_s: 速度（米/秒）
            
        Returns:
            配速字符串，如 "6'30\""
        """
        if speed_m_per_s <= 0:
            return "0'00\""
        
        # 计算每公里所需秒数
        seconds_per_km = 1000 / speed_m_per_s
        minutes = int(seconds_per_km // 60)
        seconds = int(seconds_per_km % 60)
        
        return f"{minutes}'{seconds:02d}\""
    
    def _calculate_pace_from_distance_time(self, distance_m: float, duration_sec: float) -> str:
        """
        根据距离和时间计算配速
        
        Args:
            distance_m: 距离（米）
            duration_sec: 时间（秒）
            
        Returns:
            配速字符串
        """
        if distance_m <= 0 or duration_sec <= 0:
            return "0'00\""
        
        # 计算每公里所需秒数
        seconds_per_km = duration_sec / (distance_m / 1000)
        minutes = int(seconds_per_km // 60)
        seconds = int(seconds_per_km % 60)
        
        return f"{minutes}'{seconds:02d}\""

    def format_running_data(self, activities: List[Dict[str, Any]], fetch_details: bool = False) -> Dict[str, Any]:
        """
        格式化跑步数据为 Hugo 所需格式
        包含 VDOT 跑力和训练负荷计算

        Args:
            activities: 跑步活动数据
            fetch_details: 是否获取详细数据（分段、记圈等）

        Returns:
            格式化后的数据
        """
        stats = {
            'total_runs': len(activities),
            'total_distance': 0,
            'total_duration': '0小时0分钟',
            'avg_pace': "0'00\"",
            'longest_run': 0,
            'avg_vdot': 0,
            'total_training_load': 0
        }

        total_seconds = 0
        total_vdot = 0
        vdot_count = 0
        formatted_runs = []

        for activity in activities:
            distance = activity.get('distance', 0) / 1000  # 转换为公里
            distance_meters = activity.get('distance', 0)
            duration_seconds = activity.get('duration', 0)
            avg_hr = activity.get('averageHR', 0)
            
            # 获取最大心率
            max_hr = activity.get('maxHR', 0)
            
            # 获取步频（转换为步/分钟）
            cadence = activity.get('avgRunningCadenceInStepsPerMinute', 0)
            
            # 获取步幅（米）
            stride_length = activity.get('avgStrideLength', 0)
            
            # 获取功率数据
            avg_power = activity.get('avgPower', 0)
            max_power = activity.get('maxPower', 0)
            
            # 获取卡路里
            calories = activity.get('calories', 0)
            
            # 获取爬升数据
            elevation_gain = activity.get('elevationGain', 0)

            # 计算配速（分钟/公里）
            pace_seconds = duration_seconds / distance if distance > 0 else 0
            pace_minutes = int(pace_seconds // 60)
            pace_remaining_seconds = int(pace_seconds % 60)
            pace = f"{pace_minutes}'{pace_remaining_seconds:02d}\""

            # 格式化持续时间
            duration_minutes = int(duration_seconds // 60)
            duration_hours = duration_minutes // 60
            duration_remaining_minutes = duration_minutes % 60
            if duration_hours > 0:
                duration_str = f"{duration_hours}小时{duration_remaining_minutes}分钟"
            else:
                duration_str = f"{duration_remaining_minutes}分钟"

            # 计算 VDOT 和训练负荷
            vdot = self.vdot_calculator.calculate_vdot(distance_meters, duration_seconds, avg_hr)
            training_load = self.vdot_calculator.calculate_training_load(duration_seconds, avg_hr)

            # 更新统计数据
            stats['total_distance'] += distance
            stats['longest_run'] = max(stats['longest_run'], distance)
            stats['total_training_load'] += training_load
            total_seconds += duration_seconds

            if vdot:
                total_vdot += vdot
                vdot_count += 1

            # 获取训练名称
            workout_name = self._get_workout_name(activity)
            
            # 获取心率区间
            hr_zone = self.vdot_calculator.get_hr_zone(avg_hr) if avg_hr > 0 else 0
            
            # 创建格式化的跑步记录
            run_data = {
                'date': activity.get('startTimeLocal', ''),
                'distance': round(distance, 2),
                'duration': duration_str,
                'pace': pace,
                'heart_rate': round(avg_hr, 1) if avg_hr else 0,
                'max_heart_rate': round(max_hr, 1) if max_hr else 0,
                'cadence': round(cadence) if cadence else 0,
                'stride_length': round(stride_length, 2) if stride_length else 0,
                'avg_power': round(avg_power) if avg_power else 0,
                'max_power': round(max_power) if max_power else 0,
                'calories': round(calories) if calories else 0,
                'elevation_gain': round(elevation_gain, 1) if elevation_gain else 0,
                'route': activity.get('locationName', '未知路线'),
                'weather': self._get_weather_info(activity),
                'activity_type': self._get_activity_type(activity),
                'workout_name': workout_name,
                'vdot': vdot,
                'training_load': training_load,
                'hr_zone': hr_zone
            }
            
            # 获取详细数据（如果需要）
            if fetch_details:
                activity_id = activity.get('activityId')
                if activity_id:
                    details = self._get_activity_details(activity_id)
                    run_data['segments'] = details['segments']
                    run_data['laps'] = details['laps']
                    # 调试日志
                    if details['segments']:
                        logger.info(f"活动 {activity_id}: 获取到 {len(details['segments'])} 个分段, {len(details['laps'])} 个记圈")

            formatted_runs.append(run_data)

        # 计算平均配速
        if stats['total_distance'] > 0:
            avg_pace_seconds = total_seconds / stats['total_distance']
            avg_pace_minutes = int(avg_pace_seconds // 60)
            avg_pace_remaining_seconds = int(avg_pace_seconds % 60)
            stats['avg_pace'] = f"{avg_pace_minutes}'{avg_pace_remaining_seconds:02d}\""

        # 计算平均 VDOT
        if vdot_count > 0:
            stats['avg_vdot'] = round(total_vdot / vdot_count, 1)

        # 格式化总持续时间
        total_minutes = int(total_seconds // 60)
        total_hours = total_minutes // 60
        total_remaining_minutes = total_minutes % 60
        stats['total_duration'] = f"{total_hours}小时{total_remaining_minutes}分钟"

        # 保留一位小数
        stats['total_distance'] = round(stats['total_distance'], 1)
        stats['longest_run'] = round(stats['longest_run'], 1)

        # 按日期排序（最新的在前）
        formatted_runs.sort(key=lambda x: x['date'], reverse=True)

        return {
            'stats': stats,
            'runs': formatted_runs
        }

    def _get_weather_info(self, activity: Dict[str, Any]) -> str:
        """
        获取天气信息

        Args:
            activity: 活动数据

        Returns:
            天气信息字符串
        """
        # 尝试从活动数据中获取天气信息
        weather = activity.get('weather', {})
        if weather:
            temperature = weather.get('temperature', {})
            if temperature:
                temp_c = temperature.get('c', 0)
                condition = weather.get('condition', '未知')
                return f"{condition}，{temp_c}°C"

        return "未知天气"

    def save_to_hugo_data(self, data: Dict[str, Any], output_path: str = "data/running.json", merge: bool = True) -> bool:
        """
        保存数据到 Hugo 数据文件

        Args:
            data: 格式化后的数据
            output_path: 输出文件路径
            merge: 是否与现有数据合并（增量更新）

        Returns:
            是否保存成功
        """
        try:
            # 确保目录存在
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            # 如果需要合并且文件已存在
            if merge and os.path.exists(output_path):
                try:
                    with open(output_path, 'r', encoding='utf-8') as f:
                        existing_data = json.load(f)

                    # 合并数据
                    merged_data = self._merge_running_data(existing_data, data)
                    data = merged_data
                    logger.info(f"已与现有数据合并，共 {len(data['runs'])} 条跑步记录")
                except Exception as e:
                    logger.warning(f"合并现有数据失败，将覆盖文件: {e}")

            # 保存 JSON 文件
            with open(output_path, 'w', encoding='utf-8') as f:
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
        if run_a.get('date') == run_b.get('date'):
            return True

        # 2. 同一天 + 同距离 + 同时长
        date_a = run_a.get('date', '').split(' ')[0]
        date_b = run_b.get('date', '').split(' ')[0]
        if date_a and date_a == date_b:
            distance_a = run_a.get('distance', 0)
            distance_b = run_b.get('distance', 0)
            duration_a = run_a.get('duration', '')
            duration_b = run_b.get('duration', '')
            if (distance_a == distance_b and
                duration_a == duration_b and
                distance_a is not None and distance_a > 0):
                return True

        return False

    def _deduplicate_runs(self, runs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        对跑步记录列表进行去重
        """
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

    def _merge_running_data(self, existing_data: Dict[str, Any], new_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        合并跑步数据

        Args:
            existing_data: 现有数据
            new_data: 新数据

        Returns:
            合并后的数据
        """
        existing_runs = existing_data.get('runs', [])

        # 先对现有数据去重（防止历史数据已存在重复）
        existing_runs = self._deduplicate_runs(existing_runs)

        # 处理新跑步记录
        for new_run in new_data.get('runs', []):
            matched = False
            for existing_run in existing_runs:
                if self._is_same_run(existing_run, new_run):
                    # 更新现有记录
                    for key, value in new_run.items():
                        if key == 'date':
                            # 日期字段保留原值（用于标识）
                            pass
                        elif key not in existing_run:
                            # 字段不存在，直接添加
                            existing_run[key] = value
                        elif key in ['segments', 'laps']:
                            # 对于 segments 和 laps，如果新数据有内容则覆盖
                            if value and len(value) > 0:
                                existing_run[key] = value
                        else:
                            # 其他字段：如果新数据有值则更新，否则保留旧值
                            if value and value != 0 and value != '0\'00"':
                                existing_run[key] = value
                    matched = True
                    break

            if not matched:
                # 添加新记录
                existing_runs.append(new_run)

        # 最终去重（防止新数据内部或合并后产生重复）
        existing_runs = self._deduplicate_runs(existing_runs)

        # 按日期排序（最新的在前）
        existing_runs.sort(key=lambda x: x['date'], reverse=True)
        existing_data['runs'] = existing_runs

        # 重新计算统计数据
        existing_data['stats'] = self._recalculate_stats(existing_data['runs'])

        return existing_data

    def _recalculate_stats(self, runs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        重新计算统计数据
        包含 VDOT 和训练负荷，以及各周期统计

        Args:
            runs: 跑步记录列表

        Returns:
            统计数据
        """
        stats = {
            'total_runs': len(runs),
            'total_distance': 0,
            'total_duration': '0小时0分钟',
            'avg_pace': "0'00\"",
            'longest_run': 0,
            'avg_vdot': 0,
            'total_training_load': 0,
            'period_stats': {}
        }

        total_seconds = 0
        total_vdot = 0
        vdot_count = 0

        for run in runs:
            distance = run['distance']
            duration_str = run['duration']

            # 更新统计数据
            stats['total_distance'] += distance
            stats['longest_run'] = max(stats['longest_run'], distance)
            
            # 累加训练负荷
            if 'training_load' in run:
                stats['total_training_load'] += run['training_load']
            
            # 累加 VDOT
            if 'vdot' in run and run['vdot']:
                total_vdot += run['vdot']
                vdot_count += 1

            # 解析持续时间字符串
            duration_parts = duration_str.replace('小时', ':').replace('分钟', '').split(':')
            if len(duration_parts) == 2:
                hours = int(duration_parts[0])
                minutes = int(duration_parts[1])
                total_seconds += hours * 3600 + minutes * 60
            else:
                minutes = int(duration_parts[0])
                total_seconds += minutes * 60

        # 计算平均配速
        if stats['total_distance'] > 0:
            avg_pace_seconds = total_seconds / stats['total_distance']
            avg_pace_minutes = int(avg_pace_seconds // 60)
            avg_pace_remaining_seconds = int(avg_pace_seconds % 60)
            stats['avg_pace'] = f"{avg_pace_minutes}'{avg_pace_remaining_seconds:02d}\""

        # 计算平均 VDOT
        if vdot_count > 0:
            stats['avg_vdot'] = round(total_vdot / vdot_count, 1)

        # 格式化总持续时间
        total_minutes = int(total_seconds // 60)
        total_hours = total_minutes // 60
        total_remaining_minutes = total_minutes % 60
        stats['total_duration'] = f"{total_hours}小时{total_remaining_minutes}分钟"

        # 保留一位小数
        stats['total_distance'] = round(stats['total_distance'], 1)
        stats['longest_run'] = round(stats['longest_run'], 1)

        # 计算各周期统计
        stats['period_stats'] = self._calculate_period_stats(runs)

        return stats

    def _calculate_period_stats(self, runs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        计算各周期（周、月、年、总）的统计数据
        
        Args:
            runs: 跑步记录列表
            
        Returns:
            各周期统计数据
        """
        from datetime import datetime, timedelta
        
        now = datetime.now()
        
        # 定义各周期的日期范围
        period_ranges = {
            'week': {
                'start': now - timedelta(days=7),
                'end': now
            },
            'month': {
                'start': datetime(now.year, now.month, 1),
                'end': now
            },
            'year': {
                'start': datetime(now.year, 1, 1),
                'end': now
            },
            'total': {
                'start': datetime.min,
                'end': now
            }
        }
        
        period_stats = {}
        
        for period_name, date_range in period_ranges.items():
            period_data = self._calculate_stats_for_period(
                runs, 
                date_range['start'], 
                date_range['end']
            )
            period_stats[period_name] = period_data
        
        return period_stats
    
    def _calculate_stats_for_period(
        self, 
        runs: List[Dict[str, Any]], 
        start_date: datetime, 
        end_date: datetime
    ) -> Dict[str, Any]:
        """
        计算指定周期内的统计数据
        
        Args:
            runs: 跑步记录列表
            start_date: 开始日期
            end_date: 结束日期
            
        Returns:
            周期统计数据
        """
        # 过滤该周期内的跑步记录
        period_runs = []
        for run in runs:
            try:
                run_date = datetime.strptime(run['date'].split(' ')[0], '%Y-%m-%d')
                if start_date <= run_date <= end_date:
                    period_runs.append(run)
            except (ValueError, IndexError):
                continue
        
        if not period_runs:
            return {
                'total_activities': 0,
                'total_distance': 0,
                'total_duration_hours': 0,
                'avg_pace': "--",
                'avg_heart_rate': None,
                'avg_vdot': None,
                'total_training_load': 0
            }
        
        # 计算统计数据
        total_distance = sum(r['distance'] for r in period_runs)
        total_activities = len(period_runs)
        total_training_load = sum(r.get('training_load', 0) for r in period_runs)
        
        # 计算总时长（秒）
        total_seconds = 0
        total_hr = 0
        hr_count = 0
        total_vdot = 0
        vdot_count = 0
        
        for run in period_runs:
            # 解析时长
            duration_str = run['duration']
            duration_parts = duration_str.replace('小时', ':').replace('分钟', '').split(':')
            if len(duration_parts) == 2:
                hours = int(duration_parts[0])
                minutes = int(duration_parts[1])
                total_seconds += hours * 3600 + minutes * 60
            else:
                minutes = int(duration_parts[0])
                total_seconds += minutes * 60
            
            # 累加心率
            hr = run.get('heart_rate', 0)
            if hr and hr > 0:
                total_hr += hr
                hr_count += 1
            
            # 累加 VDOT
            vdot = run.get('vdot')
            if vdot and vdot > 0:
                total_vdot += vdot
                vdot_count += 1
        
        # 计算平均配速
        if total_distance > 0:
            avg_pace_seconds = total_seconds / total_distance
            avg_pace_minutes = int(avg_pace_seconds // 60)
            avg_pace_remaining_seconds = int(avg_pace_seconds % 60)
            avg_pace = f"{avg_pace_minutes}'{avg_pace_remaining_seconds:02d}\""
        else:
            avg_pace = "--"
        
        # 计算平均心率
        avg_hr = round(total_hr / hr_count) if hr_count > 0 else None
        
        # 计算平均 VDOT
        avg_vdot = round(total_vdot / vdot_count, 1) if vdot_count > 0 else None
        
        # 总时长（小时）
        total_hours = round(total_seconds / 3600, 1)
        
        return {
            'total_activities': total_activities,
            'total_distance': round(total_distance, 1),
            'total_duration_hours': total_hours,
            'avg_pace': avg_pace,
            'avg_heart_rate': avg_hr,
            'avg_vdot': avg_vdot,
            'total_training_load': total_training_load
        }


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='从 Garmin Connect 获取跑步数据')

    # 添加参数选项
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--days', type=int, default=30,
                       help='获取最近多少天的跑步数据 (默认: 30)')
    group.add_argument('--year', type=int,
                       help='获取指定年份的跑步数据')
    group.add_argument('--all', action='store_true',
                       help='获取所有跑步数据')

    parser.add_argument('--output', type=str, default='src/data/running.json',
                       help='输出文件路径 (默认: src/data/running.json)')
    parser.add_argument('--no-merge', action='store_true',
                       help='不与现有数据合并，直接覆盖文件')
    parser.add_argument('--email', type=str,
                       help='Garmin 账户邮箱 (也可通过环境变量 GARMIN_EMAIL 设置)')
    parser.add_argument('--password', type=str,
                       help='Garmin 账户密码 (也可通过环境变量 GARMIN_PASSWORD 设置)')
    parser.add_argument('--debug', action='store_true',
                       help='打印详细调试信息，查看活动数据结构')
    parser.add_argument('--no-details', action='store_true',
                       help='不获取详细数据（分段、记圈等），减少 API 调用次数')

    return parser.parse_args()


def main():
    """主函数"""
    # 解析命令行参数
    args = parse_args()

    # 获取账户信息
    email = args.email or os.environ.get('GARMIN_EMAIL', '')
    password = args.password or os.environ.get('GARMIN_PASSWORD', '')

    if not email or not password:
        print("请设置环境变量 GARMIN_EMAIL 和 GARMIN_PASSWORD")
        print("或者使用 --email 和 --password 参数")
        return

    # 创建数据获取器
    fetcher = GarminDataFetcher(email, password)

    # 登录
    if not fetcher.login():
        print("登录失败，请检查邮箱和密码")
        return

    # 根据参数获取不同范围的活动数据
    activities = []

    if args.all:
        # 获取所有活动数据（从最早开始）
        print("获取所有跑步数据...")
        # 这里可能需要分页获取，先获取最近一年的数据作为示例
        activities = fetcher.get_activities(days=365)
        # 如果需要获取更多数据，可以实现分页逻辑
    elif args.year:
        # 获取指定年份的数据
        print(f"获取 {args.year} 年的跑步数据...")
        current_year = datetime.now().year
        if args.year == current_year:
            # 当前年份，从年初到现在
            start_date = datetime(args.year, 1, 1).strftime("%Y-%m-%d")
            end_date = datetime.now().strftime("%Y-%m-%d")
        else:
            # 历史年份，整个年份
            start_date = datetime(args.year, 1, 1).strftime("%Y-%m-%d")
            end_date = datetime(args.year, 12, 31).strftime("%Y-%m-%d")

        # 计算天数
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days = (end - start).days + 1

        activities = fetcher.get_activities_by_date(start_date, end_date)
        logger.info(f"获取到 {len(activities)} 个活动")
    else:
        # 获取最近指定天数的数据
        print(f"获取最近 {args.days} 天的跑步数据...")
        activities = fetcher.get_activities(days=args.days)

    # 过滤跑步活动
    running_activities = fetcher.filter_running_activities(activities)
    
    # 如果是调试模式，打印更多详细信息
    if args.debug and running_activities:
        logger.info("\n调试模式：打印第一个跑步活动的完整数据")
        fetcher._print_activity_details(running_activities[0], 1)

    if not running_activities:
        print("没有找到跑步活动")
        return

    # 格式化数据（默认获取详细数据）
    running_data = fetcher.format_running_data(running_activities, fetch_details=not args.no_details)

    # 保存到 Hugo 数据文件
    merge = not args.no_merge
    if fetcher.save_to_hugo_data(running_data, args.output, merge):
        print("跑步数据获取并保存成功！")

        # 打印统计信息
        stats = running_data['stats']
        print(f"\n本次获取的跑步统计:")
        print(f"跑步次数: {stats['total_runs']}")
        print(f"跑步距离: {stats['total_distance']} 公里")
        print(f"跑步时间: {stats['total_duration']}")
        print(f"平均配速: {stats['avg_pace']}")
        print(f"最长距离: {stats['longest_run']} 公里")
        if stats.get('avg_vdot'):
            print(f"平均 VDOT: {stats['avg_vdot']}")
        if stats.get('total_training_load'):
            print(f"总训练负荷: {stats['total_training_load']}")
        
        # 打印前5条记录的详细信息（包括训练名称、VDOT、训练负荷）
        print(f"\n前5条跑步记录:")
        for i, run in enumerate(running_data['runs'][:5]):
            workout_info = f" [{run.get('workout_name', '')}]" if run.get('workout_name') else ""
            vdot_info = f" VDOT:{run['vdot']}" if run.get('vdot') else ""
            load_info = f" 负荷:{run['training_load']}" if run.get('training_load') else ""
            print(f"  {i+1}. {run['date']}: {run['distance']}km, {run['pace']}/km{workout_info}{vdot_info}{load_info}")

        # 如果是合并模式，打印总统计信息
        if merge and os.path.exists(args.output):
            try:
                with open(args.output, 'r', encoding='utf-8') as f:
                    total_data = json.load(f)
                total_stats = total_data['stats']
                print(f"\n总跑步统计:")
                print(f"总跑步次数: {total_stats['total_runs']}")
                print(f"总跑步距离: {total_stats['total_distance']} 公里")
                print(f"总跑步时间: {total_stats['total_duration']}")
                print(f"平均配速: {total_stats['avg_pace']}")
                print(f"最长距离: {total_stats['longest_run']} 公里")
                if total_stats.get('avg_vdot'):
                    print(f"平均 VDOT: {total_stats['avg_vdot']}")
                if total_stats.get('total_training_load'):
                    print(f"总训练负荷: {total_stats['total_training_load']}")
            except Exception as e:
                logger.warning(f"读取总统计数据失败: {e}")
    else:
        print("保存数据失败")


if __name__ == "__main__":
    main()