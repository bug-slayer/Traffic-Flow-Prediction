import joblib
import numpy as np
import os

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 加载保存的模型
model_path = os.path.join(project_root, 'models', 'traffic_model.joblib')
model = joblib.load(model_path)

def predict_traffic(hour, day_of_week, is_holiday):
    """
    预测给定条件下的交通流量
    
    参数:
    hour (int): 小时 (0-23)
    day_of_week (int): 星期几 (0-6,0表示星期一)
    is_holiday (int): 是否为假日 (0或1)
    
    返回:
    float: 预测的交通流量
    """
    input_data = np.array([[hour, day_of_week, is_holiday]])
    prediction = model.predict(input_data)
    return prediction[0]

if __name__ == "__main__":
    # 示例使用
    print("预测周二(1)下午3点(15)非假日(0)的交通流量:")
    print(predict_traffic(15, 1, 0))

    print("\n预测周六(5)上午10点(10)假日(1)的交通流量:")
    print(predict_traffic(10, 5, 1))