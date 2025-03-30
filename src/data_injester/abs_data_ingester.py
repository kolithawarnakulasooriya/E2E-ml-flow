import pandas as pd
from abc import ABC, abstractmethod

"""
    Abstract base class for data ingesters
"""
class DataIngester(ABC):

    """
        This is the core abstract ingest method
    """
    @abstractmethod
    def ingest(self, file_path:str) -> pd.DataFrame:
        pass