import unittest
import sys
import os

# 将项目根目录添加到 Python 路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.predict.predict_traffic import predict_traffic

class TestPredictTraffic(unittest.TestCase):
    def setUp(self):
        # 在这里可以添加一些测试前的准备工作,如果需要的话
        pass

    def test_predict_traffic_weekday(self):
        # 测试工作日的预测
        prediction = predict_traffic(hour=8, day_of_week=1, is_holiday=0)
        self.assertIsInstance(prediction, (int, float))
        self.assertGreater(prediction, 0)

    def test_predict_traffic_weekend(self):
        # 测试周末的预测
        prediction = predict_traffic(hour=12, day_of_week=6, is_holiday=0)
        self.assertIsInstance(prediction, (int, float))
        self.assertGreater(prediction, 0)

    def test_predict_traffic_holiday(self):
        # 测试假日的预测
        prediction = predict_traffic(hour=15, day_of_week=2, is_holiday=1)
        self.assertIsInstance(prediction, (int, float))
        self.assertGreater(prediction, 0)

    def test_invalid_input(self):
        # 测试无效输入
        with self.assertRaises(ValueError):
            predict_traffic(hour=24, day_of_week=7, is_holiday=2)

if __name__ == '__main__':
    unittest.main()