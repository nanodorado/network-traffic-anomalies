import unittest
from anomaly_detection import detect_anomalies
import pandas as pd

class TestAnomalyDetection(unittest.TestCase):
    def test_detect_anomalies(self):
        test_data = pd.DataFrame({
            'src_bytes': [1, 2, 3, 4, 5],
            'dst_bytes': [5, 4, 3, 2, 1]
        })
        result = detect_anomalies(test_data, ['src_bytes', 'dst_bytes'])
        self.assertIsNotNone(result)
        self.assertIn('scores', result.columns)
        self.assertIn('anomaly', result.columns)

if __name__ == '__main__':
    unittest.main()