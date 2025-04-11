from abc import ABC, abstractmethod
import pandas as pd
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OutlierDetector(ABC):
    """
    Abstract base class for outlier detection and handling methods.
    """

    @abstractmethod
    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Detect outliers in the given data.

        Parameters:
        df (pd.DataFrame): The input data.

        Returns:
        pd.DataFrame: A DataFrame containing the detected outliers.
        """
        pass

class ZScoreOutlierDetector(OutlierDetector):
    """
    Outlier detection using Z-Score method.
    """

    def __init__(self, threshold: float = 3.0):
        self.threshold = threshold

    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Detect outliers using Z-Score method.

        Parameters:
        df (pd.DataFrame): The input data.

        Returns:
        pd.DataFrame: A DataFrame containing the detected outliers.
        """
        logging.info("Detecting outliers using Z-Score method.")
        mean = df.mean()
        std_dev = df.std()
        z_scores = (df - mean) / std_dev
        outliers = (z_scores > self.threshold) | (z_scores < -self.threshold)
        logging.info("Outliers detected using Z-Score method.")
        return outliers
    
class IQROutlierDetector(OutlierDetector):
    """
    Outlier detection using Interquartile Range (IQR) method.
    """

    def __init__(self, factor: float = 1.5):
        self.factor = factor

    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Detect outliers using IQR method.

        Parameters:
        df (pd.DataFrame): The input data.

        Returns:
        pd.DataFrame: A DataFrame containing the detected outliers.
        """
        logging.info("Detecting outliers using IQR method.")
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - self.factor * IQR
        upper_bound = Q3 + self.factor * IQR
        outliers = (df < lower_bound) | (df > upper_bound)
        logging.info("Outliers detected using IQR method.")
        return outliers
    
class OutlierDetectorFactory:
    """
    Factory class for creating outlier detectors.
    """

    @staticmethod
    def create_detector(method: str, extra: float) -> OutlierDetector:
        """
        Create an outlier detector based on the specified method.

        Parameters:
        method (str): The method to use for outlier detection ('zscore' or 'iqr').
        df (pd.DataFrame): The input data.
        extra (float): The extra parameters to use for the methods.

        Returns:
        OutlierDetector: An instance of the specified outlier detector.
        """
        if method == 'zscore':
            return ZScoreOutlierDetector(threshold=extra)
        elif method == 'iqr':
            return IQROutlierDetector(factor=extra)
        else:
            raise ValueError(f"Unknown method: {method}")
        

class OutlierHandler:
    """
    Class for handling outliers in data.
    """

    def __init__(self, method: str, extra: float):
        self.detector = OutlierDetectorFactory.create_detector(method, extra)

    def handle_outliers(self, method:str, df: pd.DataFrame) -> pd.DataFrame:
        """
        Handle outliers in the given data.

        Parameters:
        method (str): The method to use for outlier handling ('remove' or 'cap').
        df (pd.DataFrame): The input data.

        Returns:
        pd.DataFrame: A DataFrame with outliers handled.
        """
        logging.info("Handling outliers in the data.")
        outliers = self.detector.detect_outliers(df.select_dtypes(include=[int, float]))
        df_cleaned = df.copy()
        if method == 'remove':
            df_cleaned = df_cleaned[~outliers.all(axis=1)]
        else:
            raise ValueError(f"Unknown method: {method}")

        logging.info("Outliers handled in the data.")
        return df_cleaned