import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# 设置随机种子以确保可重复性
np.random.seed(42)

# 生成日期范围
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='H')

# 创建数据框
df = pd.DataFrame({
    'datetime': date_range,
    'hour': date_range.hour,
    'day_of_week': date_range.dayofweek,
    'is_holiday': np.random.choice([0, 1], size=len(date_range), p=[0.97, 0.03])  # 假设3%的日子是假日
})

# 生成模拟的交通流量数据
base_volume = 1000
hour_effect = np.sin(df['hour'] * 2 * np.pi / 24) * 500 + 500  # 模拟每天的交通模式
weekday_effect = np.where(df['day_of_week'] < 5, 200, -200)  # 工作日交通更多
holiday_effect = np.where(df['is_holiday'] == 1, -300, 0)  # 假日交通较少
random_effect = np.random.normal(0, 100, size=len(df))  # 随机波动

df['traffic_volume'] = (base_volume + hour_effect + weekday_effect + holiday_effect + random_effect).astype(int)
df['traffic_volume'] = df['traffic_volume'].clip(lower=0)  # 确保交通流量非负

# 保存数据集
output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'raw', 'traffic_data.csv')
df.to_csv(output_path, index=False)

print(f"数据集已生成并保存为 '{output_path}'")