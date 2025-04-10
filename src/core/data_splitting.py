from abc import ABC, abstractmethod
import pandas as pd
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataSplittingStrategy(ABC):
    """
    Abstract base class for data splitting strategies.
    """

    @abstractmethod
    def split_data(self, df: pd.DataFrame, target_coumn: str) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Split the data into training and testing sets.

        Parameters:
        df (pd.DataFrame): The input data.
        target_column (str): The target column name.

        Returns:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]: A tuple containing the training and testing sets. 
        """
        pass

class BasicDataSplittingStrategy(DataSplittingStrategy):
    """
    Basic data splitting strategy that splits the data into training and testing sets.
    """

    def __init__(self, test_size: float = 0.2, random_state: int = 1):
        """
        Initialize the BasicDataSplittingStrategy.

        Parameters:
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): Random state for reproducibility.
        """
        self.test_size = test_size
        self.random_state = random_state

    def split_data(self, df: pd.DataFrame, target_coumn: str) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Split the data into training and testing sets.

        Parameters:
        df (pd.DataFrame): The input data.
        target_column (str): The target column name.

        Returns:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]: A tuple containing the training and testing sets.
        """

        if df is None or not isinstance(df, pd.DataFrame) or df.empty:
            raise ValueError("Input DataFrame is empty or None.")
        
        if not (0 < self.test_size < 1):
            raise ValueError("test_size must be between 0 and 1.")

        logging.info("Splitting data into training and testing sets.")
        X = df.drop(columns=[target_coumn])
        y = df[target_coumn]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)
        logging.info("Data splitting completed.")
        logging.debug(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
        return X_train, X_test, y_train, y_test
    
class DataSplitterFactory:
    """
    Factory class to create data splitting strategies.
    """

    @staticmethod
    def create_data_splitter(strategy_type: str, test_size: float = 0.2, random_state: int = 1) -> DataSplittingStrategy:
        """
        Create a data splitting strategy.

        Parameters:
        strategy_type (str): The type of data splitting strategy ('basic' or 'stratified').
        kwargs: Additional parameters for the strategy.

        Returns:
        DataSplittingStrategy: An instance of the specified data splitting strategy.
        """
        if strategy_type == "basic":
            return BasicDataSplittingStrategy(test_size=test_size, random_state=random_state)
        else:
            raise ValueError(f"Unknown strategy type: {strategy_type}")
        
class DataSplitter:
    """
    Class to handle data splitting using different strategies.
    """

    def __init__(self, strategy_type: str, test_size: float = 0.2, random_state: int = 1):
        """
        Initialize the DataSplitter.

        Parameters:
        strategy (DataSplittingStrategy): The data splitting strategy to use.
        """
        self.strategy = DataSplitterFactory.create_data_splitter(strategy_type, test_size, random_state)

    def split_data(self, df: pd.DataFrame, target_column: str) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Split the data into training and testing sets.

        Parameters:
        df (pd.DataFrame): The input data.
        target_column (str): The target column name.

        Returns:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]: A tuple containing the training and testing sets.
        """
        if target_column not in df.columns:
            raise ValueError(f"Target column '{target_column}' not found in DataFrame.")
        return self.strategy.split_data(df, target_column)