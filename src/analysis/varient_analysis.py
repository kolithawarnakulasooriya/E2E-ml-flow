from .abs_variate_analyse_strategy import UniVariantAnalyzeStategy, BiVariantAnalyzeStategy, MultiVariantAnalyzeStategyTemplate
from matplotlib import pyplot as plt
from seaborn import histplot, countplot,scatterplot, boxplot, heatmap, pairplot
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

class BasicMultiVarientAnalysis(MultiVariantAnalyzeStategyTemplate):

    def generate_corr_heatmap(self, df):
        plt.figure(figsize=(10,8))
        heatmap(data=df.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title(f"Correlation Heatmap")
        plt.show()
    
    def generate_pairplot(self, df):
        plt.figure(figsize=(10,8))
        pairplot(data=df)
        plt.title("Pairplot of Selected Features")
        plt.show()