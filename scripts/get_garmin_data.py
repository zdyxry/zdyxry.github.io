#!/usr/bin/env python3
# /// script
# dependencies = [
#   "garminconnect>=0.1.20",
#   "python-dotenv>=0.19.0",
# ]
# ///
"""
使用 garminconnect 获取跑步数据并生成 Hugo 数据文件
"""

import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any
import os
import sys
import argparse

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

    def format_running_data(self, activities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        格式化跑步数据为 Hugo 所需格式

        Args:
            activities: 跑步活动数据

        Returns:
            格式化后的数据
        """
        stats = {
            'total_runs': len(activities),
            'total_distance': 0,
            'total_duration': '0小时0分钟',
            'avg_pace': "0'00\"",
            'longest_run': 0
        }

        total_seconds = 0
        formatted_runs = []

        for activity in activities:
            distance = activity.get('distance', 0) / 1000  # 转换为公里
            duration_seconds = activity.get('duration', 0)

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

            # 更新统计数据
            stats['total_distance'] += distance
            stats['longest_run'] = max(stats['longest_run'], distance)
            total_seconds += duration_seconds

            # 获取训练名称
            workout_name = self._get_workout_name(activity)
            
            # 创建格式化的跑步记录
            run_data = {
                'date': activity.get('startTimeLocal', '').split('T')[0],
                'distance': round(distance, 1),
                'duration': duration_str,
                'pace': pace,
                'heart_rate': activity.get('averageHR', 0),
                'cadence': activity.get('avgRunningCadenceInStepsPerMinute', 0),
                'route': activity.get('locationName', '未知路线'),
                'weather': self._get_weather_info(activity),
                'activity_type': self._get_activity_type(activity),
                'workout_name': workout_name
            }

            formatted_runs.append(run_data)

        # 计算平均配速
        if stats['total_distance'] > 0:
            avg_pace_seconds = total_seconds / stats['total_distance']
            avg_pace_minutes = int(avg_pace_seconds // 60)
            avg_pace_remaining_seconds = int(avg_pace_seconds % 60)
            stats['avg_pace'] = f"{avg_pace_minutes}'{avg_pace_remaining_seconds:02d}\""

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

    def _merge_running_data(self, existing_data: Dict[str, Any], new_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        合并跑步数据

        Args:
            existing_data: 现有数据
            new_data: 新数据

        Returns:
            合并后的数据
        """
        # 获取现有跑步记录的日期到记录的映射
        existing_runs_map = {run['date']: run for run in existing_data.get('runs', [])}

        # 处理新跑步记录
        for new_run in new_data.get('runs', []):
            if new_run['date'] in existing_runs_map:
                # 更新现有记录，添加新字段
                existing_run = existing_runs_map[new_run['date']]
                # 只更新缺失的字段，保留现有数据
                for key, value in new_run.items():
                    if key not in existing_run:
                        existing_run[key] = value
            else:
                # 添加新记录
                existing_data['runs'].append(new_run)

        # 按日期排序（最新的在前）
        existing_data['runs'].sort(key=lambda x: x['date'], reverse=True)

        # 重新计算统计数据
        existing_data['stats'] = self._recalculate_stats(existing_data['runs'])

        return existing_data

    def _recalculate_stats(self, runs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        重新计算统计数据

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
            'longest_run': 0
        }

        total_seconds = 0

        for run in runs:
            distance = run['distance']
            duration_str = run['duration']

            # 更新统计数据
            stats['total_distance'] += distance
            stats['longest_run'] = max(stats['longest_run'], distance)

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

        # 格式化总持续时间
        total_minutes = int(total_seconds // 60)
        total_hours = total_minutes // 60
        total_remaining_minutes = total_minutes % 60
        stats['total_duration'] = f"{total_hours}小时{total_remaining_minutes}分钟"

        # 保留一位小数
        stats['total_distance'] = round(stats['total_distance'], 1)
        stats['longest_run'] = round(stats['longest_run'], 1)

        return stats


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

    # 格式化数据
    running_data = fetcher.format_running_data(running_activities)

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
        
        # 打印前5条记录的详细信息（包括训练名称）
        print(f"\n前5条跑步记录:")
        for i, run in enumerate(running_data['runs'][:5]):
            workout_info = f" [{run.get('workout_name', '')}]" if run.get('workout_name') else ""
            print(f"  {i+1}. {run['date']}: {run['distance']}km, {run['pace']}/km{workout_info}")

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
            except Exception as e:
                logger.warning(f"读取总统计数据失败: {e}")
    else:
        print("保存数据失败")


if __name__ == "__main__":
    main()