import unittest
from main import check_suspicious_ips, temporal_analysis
import pandas as pd

class TestMainFunctions(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'timestamp': pd.date_range(start='1/1/2021', periods=24, freq='H'),
            'src_ip': ['192.168.1.100', '10.0.0.1'] * 12
        })

    def test_check_suspicious_ips(self):
        result = check_suspicious_ips(self.data, 'src_ip')
        self.assertFalse(result.empty)

    def test_temporal_analysis(self):
        result = temporal_analysis(self.data)
        self.assertEqual(len(result), 24)

if __name__ == '__main__':
    unittest.main()