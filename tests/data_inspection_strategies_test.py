import unittest
import pandas as pd
from src.analysis.basic_data_inspection import DataTypesInspectionStrategy

class TestDataTypesInspectionStrategy(unittest.TestCase):

    def test_inspect_method_with_none_dataframe(self):
        strategy = DataTypesInspectionStrategy()
        self.assertRaises(ValueError, strategy.inspect, None)


    def test_inspect_method_with_dataframe(self):
        strategy = DataTypesInspectionStrategy()
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.inspect(df)
        self.assertTrue(True)
        


if __name__ == '__main__':
    unittest.main()