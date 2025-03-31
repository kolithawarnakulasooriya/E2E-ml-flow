import pandas as pd
from typing import List
from .abs_data_inspection_strategy import DataInspectionStrategy

class Inspector:
    """_summary_
    Run the inspection with multiple strategies
    """
    def __init__(self, df:pd.DataFrame) -> None:
        self.__df = df
        self.__strategies: List[DataInspectionStrategy] = []

    def add_strategy(self, strategy: DataInspectionStrategy):
        self.__strategies.append(strategy)
        return self
    
    def execute(self) -> None:
        for strategy in self.__strategies:
            strategy.inspect(self.__df)

    

