import unittest
import pandas as pd
from unittest.mock import patch
from src.analysis.basic_data_inspection import DataTypesInspectionStrategy, DataSummaryInspectionStrategy
from src.analysis.inspection_decorator import Inspector

class TestDataTypesInspectionStrategy(unittest.TestCase):

    def test_inspect_method_with_none_dataframe(self):
        strategy = DataTypesInspectionStrategy()
        self.assertRaises(ValueError, strategy.inspect, None)


    def test_inspect_method_with_dataframe(self):
        strategy = DataTypesInspectionStrategy()
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.inspect(df)
        self.assertTrue(True)

class TestSummaryInspectionStrategy(unittest.TestCase):

    def test_inspect_method_with_none_dataframe(self):
        strategy = DataSummaryInspectionStrategy()
        self.assertRaises(ValueError, strategy.inspect, None)


    def test_inspect_method_with_dataframe(self):
        strategy = DataSummaryInspectionStrategy()
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.inspect(df)
        self.assertTrue(True)
        
class TestInspector(unittest.TestCase):

    @patch('src.analysis.basic_data_inspection.DataTypesInspectionStrategy') 
    def test_inspector(self, mock_inspector_strategy):

        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        i = Inspector(df)
        i.add_strategy(mock_inspector_strategy)
        i.execute()

        mock_inspector_strategy.inspect.assert_called()

if __name__ == '__main__':
    unittest.main()