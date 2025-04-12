from abc import ABC, abstractmethod
import pandas as pd
import logging
import numpy as np
from sklearn.preprocessing import StandardScaler
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FeatureEngineeringStrategy(ABC):

    def __init__(self, feature_set: list| None):
        """
        Initialize the feature engineering strategy.

        Parameters:
        - feature_set: The set of features to be engineered.
        """
        self.feature_set = feature_set

    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """ transform the DataFrame using the feature engineering strategy.
        Parameters: df: The DataFrame to be transformed.
        Returns: The transformed DataFrame.
        """
        pass
    
class NumericalFeatureSelection(FeatureEngineeringStrategy):
    """Numerical feature selection strategy for feature engineering."""
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Select numerical features from the DataFrame."""
        logging.info(f"Selecting numerical features: {self.feature_set}")
        df_transformed = df.copy()
        df_transformed = df_transformed.select_dtypes(include=[np.number])
        logging.info(f"Numerical features selected: {df_transformed.columns.tolist()}")
        return df_transformed
    
class CustomFeatureSelection(FeatureEngineeringStrategy):
    """Custom feature selection strategy for feature engineering."""
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Select numerical features from the DataFrame."""
        logging.info(f"Selecting custom features: {self.feature_set}")
        df_transformed = df.copy()
        df_transformed = df_transformed[self.feature_set]
        logging.info(f"Custom features selected: {df_transformed.columns.tolist()}")
        return df_transformed

class LogTransformation(FeatureEngineeringStrategy):
    """Log transformation strategy for feature engineering."""

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply log transformation to the specified features."""

        logging.info(f"Applying log transformation to features: {self.feature_set}")

        df_transformed = df.copy()
        for feature in self.feature_set:
            df_transformed[feature] = np.log1p(df_transformed[feature])

        logging.info(f"Log transformation applied to features: {self.feature_set}")
        return df_transformed
    
class StandardScalerTransformation(FeatureEngineeringStrategy):
    """StandardScaler strategy for feature engineering."""
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply standard scaling to the specified features.
        df: The DataFrame to be transformed.
        """
        logging.info(f"Applying standard scaling to features: {self.feature_set}")
        df_transformed = df.copy()
        scaler = StandardScaler()
        for feature in self.feature_set:
            df_transformed[feature] = scaler.fit_transform(df_transformed[[feature]])

        logging.info(f"Standard scaling applied to features: {self.feature_set}")
        return df_transformed

class FeatureEngineeringFactory():
    """Factory class for creating feature engineering strategies."""

    @staticmethod
    def create_strategy(strategy_type: str, feature_set: list | None) -> FeatureEngineeringStrategy:
        """Create a feature engineering strategy based on the type.
        Parameters:
        - strategy_type: The type of feature engineering strategy. 
        - feature_set: The set of features to be engineered.
        Returns: An instance of the specified feature engineering strategy.
        """
        if strategy_type == "log":
            return LogTransformation(feature_set)
        elif strategy_type == "standard":
            return StandardScalerTransformation(feature_set)
        elif strategy_type == "numerical":
            return NumericalFeatureSelection(feature_set)
        elif strategy_type == "custom":
            return CustomFeatureSelection(feature_set)
        else:
            raise ValueError(f"Unknown strategy type: {strategy_type}")