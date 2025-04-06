from abc import ABC, abstractmethod
import pandas as pd
import logging
from random import randint
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(name)s:%(message)s')

class MissingValueHandlingStrategy(ABC):
    """Abstract interface for missing values handler
    """
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

class DropMissingValues(MissingValueHandlingStrategy):
    """Perform removing the missing values from the dataframe
    """
    def __init__(self, axis=0, threshold: None = None):
        """Drop missing values in a axix of any data frame

        Args:
            axis (int, optional): axix of the data frame, 0 is row, 1 is column. Defaults to 0.
            threshold (None, optional): Require that many non-NA values . Defaults to None.
        """
        self.axis: str = axis
        self.threshold: int | None = threshold

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """perform dropping the missing data values

        Args:
            df (pd.DataFrame): input dataframe

        Returns:
            pd.DataFrame: cleaned dataframe without na values. 
        """
        id_ = randint(0, 3000)
        logging.info(f"Initiated:Missing value:{id_}: drop on axis {self.axis} with threshold {self.threshold}")
        cleaned_df = df.dropna(axis=self.axis, thresh=self.threshold) if self.threshold is not None else df.dropna(axis=self.axis)
        logging.info(f"Completed:Missing value:{id_}")
        return cleaned_df
    
class FillMissingValue(MissingValueHandlingStrategy):
    
    """Place valid values in missing value cells
    """
    def __init__(self, method: str="constant", fill_value = None):
        """Replace missing values with some valid values

        Args:
            method (str, optional): type of the method ("mean", "median", "mode" and "constant"). Defaults to "constant".
            fill_value (_type_, optional): when type is constant, what is the value to be replaced. Defaults to None.
        """
        self.method: str = method
        self.fill_value = fill_value

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """perform replacing the values

        Args:
            df (pd.DataFrame): input dataframe

        Returns:
            pd.DataFrame: cleaned dataframe without na values. 
        """
        id_ = randint(0, 3000)
        logging.info(f"Initiated:Fill Missing values:{id_}: used method {self.method} with values {self.fill_value}")

        cleaned_df = df.copy(deep=True)
        if self.method == 'mean':
            cols = cleaned_df.select_dtypes(include='number').columns
            mean = df[cols].mean()
            cleaned_df[cols] = cleaned_df[cols].fillna(mean)
        elif self.method == 'median':
            cols = cleaned_df.select_dtypes(include='number').columns
            median = df[cols].median()
            cleaned_df[cols] = cleaned_df[cols].fillna(median)
        elif self.method == 'mode':
            for col in cleaned_df.select_dtypes(include='number').columns:
                cleaned_df[col] = cleaned_df[col].fillna(df[col].mode(dropna=True).iloc[0])
        elif self.method == 'constant':
            cleaned_df = cleaned_df.fillna(self.fill_value)
        else:
            raise ValueError(f"Error:Fill Missing values:{id_}: method {self.method} is not allowed")

        logging.info(f"Colpleted:Fill Missing values:{id_}: used method {self.method} with values {self.fill_value}")
        return cleaned_df


class MissingValueHandlerDecorator():

    """Handle and clean the dataframe by handling missing values, and gabage values
    """
    def __init__(self):
        # list of strategies to perform operation
        self._strategies: List[MissingValueHandlingStrategy]  = list()

    def add(self, strategy: MissingValueHandlingStrategy):
        """Add the strategy to the execution list

        Args:
            strategy (MissingValueHandlingStrategy): specific strategy

        """
        self._strategies.append(strategy)
        return self

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """Perfom cleaning missing values according to the registered strategies

        Args:
            df (pd.DataFrame): input dataframe

        Returns:
            pd.DataFrame: cleaned dataframe
        """
        cleaned_df = df.copy(deep=True)

        for strategy in self._strategies:
            cleaned_df = strategy.handle(cleaned_df)
        
        return cleaned_df