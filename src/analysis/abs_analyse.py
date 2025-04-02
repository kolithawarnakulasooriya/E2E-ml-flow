from abc import ABC, abstractmethod
import pandas as pd

class Analysis(ABC):

    """
    This is the Analysis Template
    """

    @abstractmethod
    def analyse(self, df: pd.DataFrame):
        """
        Perform the analysis task
        """
        pass