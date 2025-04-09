from abc import ABC, abstractmethod
import pandas as pd
from .abs_analyse import Analysis

class UniVariantAnalyzeStategy(Analysis):
    """_summary_
    Abstract interfacce for univarient analysers
    """
    def __init__(self, option:str):
        self._options = option

class BiVariantAnalyzeStategy(Analysis):
    """_summary_
    Abstract interfacce for bivarient analysers
    """
    def __init__(self, option1: str, option2: str):
        self._options1 = option1
        self._options2 = option2

class MultiVariantAnalyzeStategyTemplate(Analysis):
    """_summary_
    Abstract template for multivarient analysers
    """
    @abstractmethod
    def generate_corr_heatmap(self, df: pd.DataFrame):
        """
        Generate heatmap of correlations of the features 

        Args:
            df (pd.DataFrame): input dataframe
        """
        pass
    
    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        """
        Generate pair plot for important features

        Args:
            df (pd.DataFrame): input dataset
        """
        pass

    def analyse(self, df: pd.DataFrame):
        """
        Perform analyis

        Args:
            df (pd.DataFrame): input dataset
        """
        self.generate_corr_heatmap(df)
        self.generate_pairplot(df)