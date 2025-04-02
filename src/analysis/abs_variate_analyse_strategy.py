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