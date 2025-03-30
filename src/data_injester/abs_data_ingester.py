import pandas as pd
from abc import ABC, abstractmethod

"""
This is the Data Ingester Class
"""
class DataIngester(ABC):

    """
        This is the core abstract ingest method
    """
    @abstractmethod
    def ingest(self, file_path:str) -> pd.DataFrame:
        pass