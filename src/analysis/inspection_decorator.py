import pandas as pd
from typing import List
from .abs_data_inspection_strategy import DataInspectionStrategy

class Inspector:
    """_summary_
    Run the inspection with multiple strategies

    Args:
        df:pd.DataFrame input dataframe
    """
    def __init__(self, df:pd.DataFrame) -> None:
        self.__df = df
        self.__strategies: List[DataInspectionStrategy] = []

    def add_strategy(self, strategy: DataInspectionStrategy):
        """_summary_
        add inspection strategy which needs to be performed
        Args:
            strategy (DataInspectionStrategy): necessary inspection strategy

        Returns:
            Inspector: current instance of Inspector object
        """
        self.__strategies.append(strategy)
        return self
    
    def execute(self) -> None:
        """_summary_
        
        Execute the strategies added to the inspector on the dataframe
        """
        for strategy in self.__strategies:
            strategy.inspect(self.__df)

    

