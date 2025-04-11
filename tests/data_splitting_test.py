import unittest
import pandas as pd
from unittest.mock import patch
from src.core.data_splitting import DataSplitter, DataSplitterFactory, BasicDataSplittingStrategy

class TestBasicDataSplittingStrategy(unittest.TestCase):

    def test_basic(self):
        df = pd.DataFrame({'test': range(1, 101)})
        strategy = BasicDataSplittingStrategy(test_size=0.2, random_state=1)
        X_train, X_test, y_train, y_test = strategy.split_data(df, target_column='test')
        self.assertEqual(len(X_train), 80)
        self.assertEqual(len(X_test), 20)
        self.assertEqual(len(y_train), 80)
        self.assertEqual(len(y_test), 20)

class TestDataSplitterFactory(unittest.TestCase):

    def test_basic_strategy(self):
        strategy = DataSplitterFactory().create_data_splitter("basic", 0.2, 1)
        self.assertIsInstance(strategy, BasicDataSplittingStrategy)

    def test_invalid_step(self):
        self.assertRaises(ValueError, DataSplitterFactory().create_data_splitter, "na", 1)

class TestDataSplitter(unittest.TestCase):

    def test_basic_strategy(self):
        df = pd.DataFrame({'test': range(1, 101)})
        strategy = DataSplitter(strategy_type='basic', test_size=0.2, random_state=1)
        X_train, y_train, X_test, y_test = strategy.split_data(df, target_column='test')
        self.assertEqual(len(X_train), 80)
        self.assertEqual(len(X_test), 80)
        self.assertEqual(len(y_train), 20) 
        self.assertEqual(len(y_test), 20)

    def test_unknown_method(self):
        df = pd.DataFrame({'test': [1,3,100]})
        self.assertRaises(ValueError, DataSplitter, strategy_type='na', test_size=0.2, random_state=1)

    def test_unknown_target_column(self):
        df = pd.DataFrame({'test': [1,3,100]})
        strategy = DataSplitter(strategy_type='basic', test_size=0.2, random_state=1)
        self.assertRaises(ValueError, strategy.split_data, df=df,  target_column='na')