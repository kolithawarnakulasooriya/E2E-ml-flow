from .abs_data_inspection_strategy import DataInspectionStrategy
import pandas as pd

class DataTypesInspectionStrategy(DataInspectionStrategy):
    """_summary_
    Perform the basic inspection of data columns and counts
    """
    
    def inspect(self, df: pd.DataFrame) -> None:
        """_summary_
        Show the basic data types and non null counts of the data set

        Args:
            df (pd.DataFrame): input dataframe
        """
        # if no dataframe avilable or null or undefined
        if isinstance(df, type(None)):
            raise ValueError("Dataframe is not avilable")

        print(df.info())
        
        

