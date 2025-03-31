import pandas as pd
from abc import ABC, abstractmethod

"""
    Abstract base class for data ingesters
"""
class DataIngester(ABC):
    @abstractmethod
    def ingest(self, file_path:str) -> pd.DataFrame:
        """_Perform any data ingestion from any data source

        Args:
            file_path (str): specific filetype

        Returns:
            pd.DataFrame: return extracted dataframe
        """
        pass