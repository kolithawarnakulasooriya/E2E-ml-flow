import unittest
import pandas as pd
from unittest.mock import patch
from src.core.outlier_handling import OutlierHandler, ZScoreOutlierDetector, IQROutlierDetector, OutlierDetectorFactory

class TestZScoreOutlierDetector(unittest.TestCase):

    def test_z_score_outlier_detection(self):
        df = pd.DataFrame({'test': [1,3,100]})
        strategy = ZScoreOutlierDetector(threshold=1.0)
        outliers = strategy.detect_outliers(df)
        expected_df = pd.DataFrame({'test': [False, False, True]})
        pd.testing.assert_frame_equal(outliers, expected_df, check_exact=False, check_dtype=False)

class TestIQROutlierDetectorDetector(unittest.TestCase):

    def test_irq_outlier_detection(self):
        df = pd.DataFrame({'test': [1,3,100]})
        strategy = IQROutlierDetector(factor=0.5)
        outliers = strategy.detect_outliers(df)
        expected_df = pd.DataFrame({'test': [False, False, True]})
        pd.testing.assert_frame_equal(outliers, expected_df, check_exact=False, check_dtype=False)

class TestOutlierDetectorFactoryFactory(unittest.TestCase):

    def test_z_score_strategy(self):
        strategy = OutlierDetectorFactory().create_detector("zscore", 1.0)
        self.assertIsInstance(strategy, ZScoreOutlierDetector)

    def test_iqr_strategy(self):
        strategy = OutlierDetectorFactory().create_detector("iqr", 1.0)
        self.assertIsInstance(strategy, IQROutlierDetector)

    def test_log_invalid_step(self):
        self.assertRaises(ValueError, OutlierDetectorFactory().create_detector, "na", 1.0)

class TestOutlierHandler(unittest.TestCase):

    def test_handle_outliers_zscore(self):
        df = pd.DataFrame({'test': [1,3,100]})
        strategy = OutlierHandler(method='zscore', extra=1.0)
        outliers = strategy.handle_outliers(method='remove', df=df)
        expected_df = pd.DataFrame({'test': [1,3]})
        pd.testing.assert_frame_equal(outliers, expected_df, check_exact=False, check_dtype=False)

    def test_handle_outliers_zscore(self):
        df = pd.DataFrame({'test': [1,3,100]})
        strategy = OutlierHandler(method='iqr', extra=0.5)
        outliers = strategy.handle_outliers(method='remove', df=df)
        expected_df = pd.DataFrame({'test': [1,3]})
        pd.testing.assert_frame_equal(outliers, expected_df, check_exact=False, check_dtype=False)

    def test_unknown_method(self):
        df = pd.DataFrame({'test': [1,3,100]})
        strategy = OutlierHandler(method='iqr', extra=0.5)
        self.assertRaises(ValueError, strategy.handle_outliers, method='na', df=df)