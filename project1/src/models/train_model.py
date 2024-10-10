import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 加载数据
data_path = os.path.join(project_root, 'data', 'raw', 'traffic_data.csv')
data = pd.read_csv(data_path)

# 准备特征和目标变量
X = data[['hour', 'day_of_week', 'is_holiday']]
y = data['traffic_volume']

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建和训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 评估模型
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'均方误差: {mse}')
print(f'R2 分数: {r2}')

# 保存模型
model_path = os.path.join(project_root, 'models', 'traffic_model.joblib')
joblib.dump(model, model_path)

print(f'模型已保存至 {model_path}')