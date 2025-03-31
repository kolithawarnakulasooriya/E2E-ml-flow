from abc import ABC, abstractmethod
import pandas as pd


class DataInspectionStrategy(ABC):
    """_summary_
        Abstract data inspection strategy 
    """
    @abstractmethod
    def inspect(self, df: pd.DataFrame) -> None:
        """_summary_

        Perform the specific inspection on the proivided dataframe

        Args:
            df (pd.Dataframe): Input dataframe
        
        Return:
            None
        """
        pass