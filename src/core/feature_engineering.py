from abc import ABC, abstractmethod
import pandas as pd
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FeatureEngineeringStrategy(ABC):

    def __init__(self, feature_set: list):
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

class LogTransformation(FeatureEngineeringStrategy):
    """Log transformation strategy for feature engineering."""

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply log transformation to the specified features."""

        logging.info(f"Applying log transformation to features: {self.feature_set}")

        df_transformed = df.copy()
        for feature in self.feature_set:
            df_transformed[feature] = np.log1p(df_transformed[feature])
        return df_transformed


class FeatureEngineeringFactory():
    """Factory class for creating feature engineering strategies."""

    @staticmethod
    def create_straegy(strategy_type: str, feature_set: list) -> FeatureEngineeringStrategy:
        """Create a feature engineering strategy based on the type.
        Parameters:
        - strategy_type: The type of feature engineering strategy. 
        - feature_set: The set of features to be engineered.
        Returns: An instance of the specified feature engineering strategy.
        """
        if strategy_type == "log":
            return LogTransformation(feature_set)
        else:
            raise ValueError(f"Unknown strategy type: {strategy_type}")