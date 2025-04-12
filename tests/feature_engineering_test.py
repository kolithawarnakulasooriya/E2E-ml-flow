import unittest
import pandas as pd
from unittest.mock import patch
from src.core.feature_engineering import (
    FeatureEngineeringFactory, LogTransformation, StandardScalerTransformation, NumericalFeatureSelection,
    CustomFeatureSelection
)

class TestLogTransformation(unittest.TestCase):

    def test_apply_log_transfomation(self):
        df = pd.DataFrame({'test': [1,3,5], 'name': ['test10', 'test20', 'test30']})
        strategy = LogTransformation(['test'])
        transformed_df = strategy.transform(df)
        expected_df = pd.DataFrame({'test': [0.693147, 1.386294, 1.791759], 'name': ['test10', 'test20', 'test30']})
        pd.testing.assert_frame_equal(transformed_df, expected_df, check_exact=False, check_dtype=False)
        
class TestNumericalFeatureSelection(unittest.TestCase):

    def test_apply_numeric_feature_transfomation(self):
        df = pd.DataFrame({'test': [1,3,5], 'name': ['test10', 'test20', 'test30']})
        strategy = NumericalFeatureSelection(None)
        transformed_df = strategy.transform(df)
        expected_df = pd.DataFrame({'test': [1,3,5]})
        pd.testing.assert_frame_equal(transformed_df, expected_df, check_exact=False, check_dtype=False)

class TestCustomFeatureSelection(unittest.TestCase):

    def test_apply_numeric_feature_transfomation(self):
        df = pd.DataFrame({'test': [1,3,5], 'name': ['test10', 'test20', 'test30']})
        strategy = CustomFeatureSelection(['test'])
        transformed_df = strategy.transform(df)
        expected_df = pd.DataFrame({'test': [1,3,5]})
        pd.testing.assert_frame_equal(transformed_df, expected_df, check_exact=False, check_dtype=False)

class TestStandardScalerTransformation(unittest.TestCase):

    def test_apply_standard_scale_transfomation(self):
        df = pd.DataFrame({'test': [1,3,5], 'name': ['test10', 'test20', 'test30']})
        strategy = StandardScalerTransformation(['test'])
        transformed_df = strategy.transform(df)
        expected_df = pd.DataFrame({'test': [-1.224745, 0.000000, 1.224745], 'name': ['test10', 'test20', 'test30']})
        pd.testing.assert_frame_equal(transformed_df, expected_df, check_exact=False, check_dtype=False)

class TestFeatureEngineeringFactory(unittest.TestCase):

    def test_log_transformation_step(self):
        strategy = FeatureEngineeringFactory().create_strategy("log", ['test'])
        self.assertIsInstance(strategy, LogTransformation)
        self.assertEqual(strategy.feature_set, ['test'])

    def test_standard_scale_transformation_step(self):
        strategy = FeatureEngineeringFactory().create_strategy("standard", ['test'])
        self.assertIsInstance(strategy, StandardScalerTransformation)
        self.assertEqual(strategy.feature_set, ['test'])

    def test_numerical_transformation_step(self):
        strategy = FeatureEngineeringFactory().create_strategy("numerical", None)
        self.assertIsInstance(strategy, NumericalFeatureSelection)
        self.assertEqual(strategy.feature_set, None)

    def test_custom_transformation_step(self):
        strategy = FeatureEngineeringFactory().create_strategy("custom", None)
        self.assertIsInstance(strategy, CustomFeatureSelection)
        self.assertEqual(strategy.feature_set, None)

    def test_log_invalid_step(self):
        self.assertRaises(ValueError, FeatureEngineeringFactory().create_strategy, "na", ['test'])

if __name__ == '__main__':
    unittest.main()