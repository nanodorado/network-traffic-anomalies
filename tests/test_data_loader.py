import unittest
from data_loader import load_data

class TestDataLoader(unittest.TestCase):
    def test_load_data_success(self):
        data = load_data('path_to_valid_test_data.csv')
        self.assertIsNotNone(data)
        self.assertFalse(data.empty)

    def test_load_data_failure(self):
        with self.assertRaises(Exception):
            load_data('non_existent_file.csv')

if __name__ == '__main__':
    unittest.main()