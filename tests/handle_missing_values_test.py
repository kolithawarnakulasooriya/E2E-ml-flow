import unittest
from unittest.mock import patch, Mock
import pandas as pd
from src.core.missing_value_handling import DropMissingValues, FillMissingValues, MissingValueHandler

class TestDropMissingValues(unittest.TestCase):

    @patch('src.core.missing_value_handling.logging')
    def test_indeitify_missing_values_in_dataframe(self, mock_log):
        strategy = DropMissingValues()
        df = pd.DataFrame({'test': [None], 'name': ['test4']})
        df_cleaned = strategy.handle(df)
        self.assertTrue(df_cleaned.empty)

class TestFillMissingValues(unittest.TestCase):

    @patch('src.core.missing_value_handling.logging')
    def test_fill_missing_values_with_mean(self, mock_log):
        strategy = FillMissingValues(method="mean")
        df = pd.DataFrame({'test': [1,2,3,None], 'name': ['test1','test2','test3','test4']})
        df_cleaned = strategy.handle(df)
        
        self.assertTrue(df_cleaned[df_cleaned['name'] == 'test4']['test'].values.item()== 2.0)

    @patch('src.core.missing_value_handling.logging')
    def test_fill_missing_values_with_median(self, mock_log):
        strategy = FillMissingValues(method="median")
        df = pd.DataFrame({'test': [1,2,3,None], 'name': ['test1','test2','test3','test4']})
        df_cleaned = strategy.handle(df)
        
        self.assertTrue(df_cleaned[df_cleaned['name'] == 'test4']['test'].values.item()== 2.0)

    @patch('src.core.missing_value_handling.logging')
    def test_fill_missing_values_with_mode(self, mock_log):
        strategy = FillMissingValues(method="mode")
        df = pd.DataFrame({'test': [2,2,3,None], 'name': ['test1','test2','test3','test4']})
        df_cleaned = strategy.handle(df)
        
        self.assertTrue(df_cleaned[df_cleaned['name'] == 'test4']['test'].values.item()== 2.0)

    @patch('src.core.missing_value_handling.logging')
    def test_fill_missing_values_with_constant(self, mock_log):
        strategy = FillMissingValues(method="constant", fill_value=4.0)
        df = pd.DataFrame({'test': [2,2,3,None], 'name': ['test1','test2','test3','test4']})
        df_cleaned = strategy.handle(df)
        
        self.assertTrue(df_cleaned[df_cleaned['name'] == 'test4']['test'].values.item()== 4.0)

    @patch('src.core.missing_value_handling.logging')
    def test_fill_missing_values_with_non_allowed_methods(self, mock_log):
        strategy = FillMissingValues(method="na")
        df = pd.DataFrame({'test': [2,2,3,None], 'name': ['test1','test2','test3','test4']})
        
        self.assertRaises(ValueError, strategy.handle, df)

class TestFillMissingValuesHandler(unittest.TestCase):

    @patch('src.core.missing_value_handling.logging')
    def test_handle_missing_values(self, mock_log):
        strategy = MissingValueHandler()
        mock_strategy_1 = DropMissingValues()
        df = pd.DataFrame({'test': [2,2,3,None], 'name': ['test1','test2','test3','test4']})
        
        clened_df = strategy.add(mock_strategy_1).handle(df)
        self.assertFalse('test4' in clened_df['name'].values)