import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from .abs_missing_value_analysis import MissingValueAnalyzerTemplate

class BasicMissingValueAnalyser(MissingValueAnalyzerTemplate):

    def indeitify_missing_values(self, df):
        """_summary_
        show the data of missing values
        Args:
            df (_type_): input dataframe
        """
        print("Basic Missing Values Identified")
        mv = df.isnull().sum()
        print(mv[mv > 0])
    
    def visualize_missing_values(self, df):
        """_summary_
        show the data of missing values in a heatmap
        Args:
            df (_type_): input dataframe
        """
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(), cbar=False, cmap='magma')
        plt.title("Missing Values")
        plt.show()
