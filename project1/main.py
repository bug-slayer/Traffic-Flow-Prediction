import os
import sys

# 将src目录添加到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_root, 'src'))

from src.data.generate_traffic_data import generate_traffic_data
from src.models.train_model import train_model
from src.predict.predict_traffic import predict_traffic

def main():
    # 生成数据
    generate_traffic_data()
    
    # 训练模型
    train_model()
    
    # 进行预测
    print("预测周二(1)下午3点(15)非假日(0)的交通流量:")
    print(predict_traffic(15, 1, 0))

    print("\n预测周六(5)上午10点(10)假日(1)的交通流量:")
    print(predict_traffic(10, 5, 1))

if __name__ == "__main__":
    main()