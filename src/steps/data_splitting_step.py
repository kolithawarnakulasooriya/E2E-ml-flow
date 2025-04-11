from pandas import DataFrame, Series
from zenml.steps import step
from src.core.data_splitting import DataSplitter
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@step
def data_splitting_step(df: DataFrame, strategy_type:str, target_column: str, test_size: float = 0.2, random_state: int = 1) -> tuple[DataFrame, DataFrame, Series, Series]:
    """
    Step to split the data into training and testing sets.

    Parameters:
    df (pd.DataFrame): The input data.
    strategy_type (str): The type of data splitting strategy ('basic' or 'stratified').
    test_size (float): The proportion of the dataset to include in the test split.

    Returns:
    tuple[pd.DataFrame, pd.DataFrame]: A tuple containing the training and testing sets.
    """
    if df is None or not isinstance(df, DataFrame) or df.empty:
        raise ValueError("Input DataFrame is empty or None.")
    
    if not (0 < test_size < 1):
        raise ValueError("test_size must be between 0 and 1.")
    
    logging.info(f"Splitting data using {strategy_type} strategy with test size {test_size}.")
    
    X_train, X_test, y_train, y_test = DataSplitter(strategy_type=strategy_type, test_size=test_size, random_state=random_state).split_data(df, target_column=target_column)
    
    logging.info(f"Data split completed. Training set size: {X_train.shape[0]}, Testing set size: {X_test.shape[0]}.")
    
    return X_train, X_test, y_train, y_test