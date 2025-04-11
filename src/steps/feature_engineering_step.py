from zenml import step
from src.core.feature_engineering import FeatureEngineeringFactory
import pandas as pd

@step
def feature_engineering_step(df: pd.DataFrame, method: str, features: list | None):
    strategy = FeatureEngineeringFactory.create_strategy(method, features)
    return strategy.transform(df)