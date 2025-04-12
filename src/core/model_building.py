from abc import ABC
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ModelBuildingStrategy(ABC):
    """ModelBuildingStrategy is an abstract base class that defines a strategy for building models.
    """
    def set_training_data(self, x_train: pd.DataFrame, y_train: pd.Series):
        """Sets the training data for the model.

        Args:
            x_train (pd.DataFrame): The features for training.
            y_train (pd.DataFrame): The target variable for training.
        """
        self.x_train = x_train
        self.y_train = y_train
        self.model_pipeline: Pipeline = None
        logging.info("Training data set successfully.")

    def get_model(self):
        """Returns the trained model.

        Returns:
            Any: The trained model.
        """
        if self.model_pipeline is None:
            raise ValueError("Model pipeline is not set. Please call build_model() first.")
        return self.model_pipeline.named_steps['model']
        
    def get_pipeline(self) -> Pipeline:
        """Returns the model pipeline.

        Returns:
            Pipeline: The model pipeline.
        """
        if self.model_pipeline is None:
            raise ValueError("Model pipeline is not set. Please call build_model() first.")
        return self.model_pipeline
    
    def fit(self) -> Pipeline:
        """Defines the model building pipeline.
        """
        if self.model_pipeline is None:
            raise ValueError("Model pipeline is not set. Please call build_model() first.")
        
        logging.info("Model training started.")
        self.model_pipeline.fit(self.x_train, self.y_train)
        logging.info("Model training completed.")
        return self.model_pipeline
    
    def build_model(self) -> Pipeline:
        """Builds a model using the provided training data.

        Returns:
            Any[BaseEstimator]: The trained model.
        """
        pass
    
class LinearRegressionModelBuildingStrategy(ModelBuildingStrategy):
    """LinearRegressionModelBuildingStrategy is a concrete implementation of ModelBuildingStrategy that builds a linear regression model.
    """
    
    def create_preprocessor(self) -> Pipeline:
        """Creates a preprocessing pipeline for the model.

        Returns:
            Pipeline: The preprocessing pipeline.
        """
        logging.info("Creating preprocessing pipeline.")
        
        all_cat_columns = self.x_train.select_dtypes(exclude=[np.number]).columns
        all_num_columns = self.x_train.select_dtypes(include=[np.number]).columns
        
        logging.info(f"Categorical columns: {all_cat_columns}")
        logging.info(f"Numerical columns: {all_num_columns}")
        
        #preprocessing pipeline
        numerical_transformer = Pipeline([
            ('imputer', SimpleImputer(strategy='mean'))
        ])
        categorical_transformer = Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('scaler', OneHotEncoder(handle_unknown='ignore'))
        ])
        
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, all_num_columns),
                ('cat', categorical_transformer, all_cat_columns)
            ]
        )
        
        return preprocessor
        
    def build_model(self) -> Pipeline:
        """Builds a linear regression model using the provided training data.

        Returns:
            LinearRegression: The trained linear regression model.
        """
        logging.info("Building Linear Regression model.")
        
        preprocessor = self.create_preprocessor()
        # Create a pipeline with preprocessing and model
        self.model_pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('model', LinearRegression())
        ])

        logging.info("Linear Regression model built successfully.")
        
        return self.model_pipeline
    
class ModelBuildFactory:
    """ModelBuildFactory is a factory class that creates model building strategies.
    """
    @staticmethod
    def create_model_strategy(strategy_type: str) -> ModelBuildingStrategy:
        """Returns a model building strategy based on the provided strategy type.

        Args:
            strategy_type (str): The type of model building strategy.

        Returns:
            ModelBuildingStrategy: The model building strategy.
        """
        if strategy_type == "linear_regression":
            return LinearRegressionModelBuildingStrategy()
        else:
            raise ValueError(f"Unknown strategy type: {strategy_type}")
        