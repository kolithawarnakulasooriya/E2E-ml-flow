from abc import ABC, abstractmethod
import pandas as pd
from .abs_analyse import Analysis

class UniVariantAnalyzeStategy(Analysis):
    """_summary_
    Abstract interfacce for varient analysers
    """
    @abstractmethod
    def setOptions(self, option: str):
        """_summary_
        set filter options
        Args:
            option (str): given options
        """
        pass