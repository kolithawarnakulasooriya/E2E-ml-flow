import unittest
import pandas as pd
from unittest.mock import patch, Mock
from src.core.model_building import LinearRegressionModelBuildingStrategy, ModelBuildFactory
from sklearn.pipeline import Pipeline

class TestLinearRegressionModelBuildingStrategyStrategy(unittest.TestCase):

    @patch('src.core.model_building.LinearRegression')
    @patch('src.core.model_building.Pipeline')
    def test_model_builder(self, mock_linear_regression, mock_pipeline):
        
        mock_linear_regression.return_value = mock_linear_regression
        mock_linear_regression.fit.return_value = None
        
        df = pd.DataFrame({'x': range(1, 101), 'y': range(1, 101)})
        strategy = LinearRegressionModelBuildingStrategy()
        strategy.set_training_data(df['x'], df['y'])
        strategy.create_preprocessor = Mock()
        strategy.create_preprocessor.return_value = Mock()
        model = strategy.build_model()
        self.assertIsNotNone(model)
        self.assertTrue(strategy.create_preprocessor.called)
        self.assertTrue(mock_pipeline.called)
    
    @patch('src.core.model_building.SimpleImputer')
    @patch('src.core.model_building.OneHotEncoder')
    @patch('src.core.model_building.ColumnTransformer')
    @patch('src.core.model_building.Pipeline')
    def test_create_preprocessor(self,mock_pipeline, mock_column_transformer, mock_one_hot_encoder, mock_simple_imputer):
        strategy = LinearRegressionModelBuildingStrategy()
        strategy.set_training_data(pd.DataFrame([1, 2, 3]), pd.Series([1, 2, 3]))
        
        pipeline = strategy.create_preprocessor()
        
        self.assertIsNotNone(pipeline)
        self.assertTrue(mock_pipeline.called)
        self.assertTrue(mock_column_transformer.called)
        self.assertTrue(mock_one_hot_encoder.called)
        self.assertTrue(mock_simple_imputer.called)
        
class TestModelBuildFactory(unittest.TestCase):

    def test_create_model_linear_regression(self):
        strategy = ModelBuildFactory.create_model_strategy("linear_regression")
        self.assertIsInstance(strategy, LinearRegressionModelBuildingStrategy)

    def test_create_invalid_model_strategy(self):
        self.assertRaises(ValueError, ModelBuildFactory.create_model_strategy, "invalid_strategy")
        
