from abc import ABC, abstractmethod
import pandas as pd
from .abs_analyse import Analysis

class MissingValueAnalyzerTemplate(Analysis):

    @abstractmethod
    def indeitify_missing_values(self, df: pd.DataFrame):
        """_summary_
        identify missing values in the dataframe

        Args:
            df (pd.DataFrame): input dataframe
        """
        pass
    
    @abstractmethod
    def visualize_missing_values(self, df: pd.DataFrame):
        """_summary_
        visualize missing values in the dataframe

        Args:
            df (pd.DataFrame): _input dataframe
        """
        pass
    
    def analyse(self, df: pd.DataFrame):

        """_summary_
         pefrom the analysis tast for the dataframe

         Args:
            df (pd.DataFrame): _input dataframe
        """
        self.indeitify_missing_values(df)
        self.visualize_missing_values(df)