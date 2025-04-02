from .abs_variate_analyse_strategy import UniVariantAnalyzeStategy
from matplotlib import pyplot as plt
from seaborn import histplot, countplot
import pandas as pd

class NumericalUnivarientAnalyzer(UniVariantAnalyzeStategy):
    """_summary_
    plots the neumerical features of the dataset
    """
    def __init__(self):
        self._options = ''

    def setOptions(self, option: str):
        """_summary_
        set the data extracting feature
        Args:
             option (str): given feature of dataset

        Returns:
            UniVariantAnalyzeStategy: self
        """
        self._options = option
        return self
    
    def analyse(self, df:pd.DataFrame):
        """_summary_
        plot the histogram distruibution of a dataset
        Args:
            df (pd.Dataframe): input dataset
        """
        plt.figure(figsize=(10,8))
        histplot(df[self._options], kde=True, bins=30)
        plt.title(f"Distribution of {self._options}")
        plt.xlabel(self._options)
        plt.ylabel("F")
        plt.show()

class CategoricalUnivarientAnalyzer(UniVariantAnalyzeStategy):
    """_summary_
    plots the neumerical features of the dataset
    """
    def __init__(self):
        self._options = ''

    def setOptions(self, option: str):
        """_summary_
        set the data extracting feature
        Args:
             option (str): given feature of dataset

        Returns:
            UniVariantAnalyzeStategy: self
        """
        self._options = option
        return self
    
    def analyse(self, df:pd.DataFrame):
        """_summary_
        plot the categorical feature distruibution of a dataset
        Args:
            df (pd.Dataframe): input dataset
        """
        plt.figure(figsize=(10,8))
        countplot(x=self._options, data=df)
        plt.title(f"Distribution of {self._options}")
        plt.xlabel(self._options)
        plt.ylabel("Count")
        plt.show()
