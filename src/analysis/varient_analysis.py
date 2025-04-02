from .abs_variate_analyse_strategy import UniVariantAnalyzeStategy, BiVariantAnalyzeStategy
from matplotlib import pyplot as plt
from seaborn import histplot, countplot,scatterplot, boxplot
import pandas as pd

class NumericalUnivarientAnalyzer(UniVariantAnalyzeStategy):
    """_summary_
    plots the neumerical features of the dataset
    """
    
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

class NumericalBiVarientAnalysis(BiVariantAnalyzeStategy):
    """_summary_
    plots the neumerical analysis between two features of the dataset
    """
    def analyse(self, df):
        plt.figure(figsize=(10,8))
        scatterplot(x=self._options1, y=self._options2, data=df)
        plt.title(f"Distribution of {self._options1} vs {self._options2}")
        plt.xlabel(self._options1)
        plt.ylabel(self._options2)
        plt.show()

class CategoricalBiVarientAnalysis(BiVariantAnalyzeStategy):
    """_summary_
    plots the categorical analysis between two features of the dataset
    """
    def analyse(self, df):
        plt.figure(figsize=(10,8))
        boxplot(x=self._options1, y=self._options2, data=df)
        plt.title(f"Distribution of {self._options1} vs {self._options2}")
        plt.xlabel(self._options1)
        plt.ylabel(self._options2)
        plt.show()
