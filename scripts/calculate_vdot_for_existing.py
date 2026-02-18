#!/usr/bin/env python3
"""
为现有的 running.json 数据计算 VDOT 和训练负荷
"""

import json
import math
import os
import re
from typing import Dict, List, Any, Optional

# 心率区间配置
MAX_HR = int(os.environ.get('MAX_HR', 190))  # 最大心率
RESTING_HR = int(os.environ.get('RESTING_HR', 55))  # 静息心率


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


def parse_duration_to_seconds(duration_str: str) -> int:
    """将时长字符串转换为秒数"""
    # 格式: "1小时22分钟" 或 "41分钟"
    hour_match = re.search(r'(\d+)小时', duration_str)
    min_match = re.search(r'(\d+)分钟', duration_str)
    
    hours = int(hour_match.group(1)) if hour_match else 0
    mins = int(min_match.group(1)) if min_match else 0
    
    return hours * 3600 + mins * 60


def parse_pace_to_seconds(pace_str: str) -> float:
    """将配速字符串转换为秒数/公里"""
    # 格式: "6'33\""
    match = re.match(r"(\d+)'(\d+)\"", pace_str)
    if match:
        mins = int(match.group(1))
        secs = int(match.group(2))
        return mins * 60 + secs
    return 0


def update_running_data(input_path: str, output_path: str):
    """更新 running.json 数据，添加 VDOT 和训练负荷"""
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    calculator = VDOTCalculator()
    
    total_vdot = 0
    vdot_count = 0
    total_training_load = 0
    
    for run in data['runs']:
        distance_km = run['distance']
        distance_meters = distance_km * 1000
        duration_seconds = parse_duration_to_seconds(run['duration'])
        avg_hr = run.get('heart_rate', 0)
        
        # 计算 VDOT
        vdot = calculator.calculate_vdot(distance_meters, duration_seconds, avg_hr)
        if vdot:
            run['vdot'] = vdot
            total_vdot += vdot
            vdot_count += 1
        else:
            run['vdot'] = None
        
        # 计算训练负荷
        training_load = calculator.calculate_training_load(duration_seconds, avg_hr)
        run['training_load'] = training_load
        total_training_load += training_load
        
        # 计算心率区间
        if avg_hr > 0:
            run['hr_zone'] = calculator.get_hr_zone(avg_hr)
        else:
            run['hr_zone'] = 0
    
    # 更新统计数据
    data['stats']['avg_vdot'] = round(total_vdot / vdot_count, 1) if vdot_count > 0 else 0
    data['stats']['total_training_load'] = total_training_load
    
    # 保存更新后的数据
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"数据已更新并保存到 {output_path}")
    print(f"\n统计信息:")
    print(f"  总跑步次数: {data['stats']['total_runs']}")
    print(f"  总距离: {data['stats']['total_distance']} km")
    print(f"  平均 VDOT: {data['stats']['avg_vdot']}")
    print(f"  总训练负荷: {data['stats']['total_training_load']}")
    
    # 打印前5条记录
    print(f"\n前5条跑步记录:")
    for i, run in enumerate(data['runs'][:5]):
        vdot_str = f"VDOT:{run['vdot']}" if run.get('vdot') else "VDOT:N/A"
        load_str = f"负荷:{run['training_load']}"
        zone_str = f"Z{run['hr_zone']}" if run.get('hr_zone') else "Z0"
        print(f"  {i+1}. {run['date']}: {run['distance']}km, {run['pace']}/km, {vdot_str}, {load_str}, {zone_str}")


if __name__ == "__main__":
    input_file = "src/data/running.json"
    output_file = "src/data/running.json"
    
    update_running_data(input_file, output_file)
