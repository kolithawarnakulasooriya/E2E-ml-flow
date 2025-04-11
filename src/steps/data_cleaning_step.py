from zenml import step
import pandas as pd
from typing import Optional
from src.core.missing_value_handling import MissingValueHandler, DropMissingValues, FillMissingValues

@step
def data_clean_and_fix(df: pd.DataFrame, method: str = 'drop', fill_value: Optional[int]=None) -> pd.DataFrame:

    """
    Handles missing values in the data
    """

    decorator = MissingValueHandler()
    
    if method == 'drop':
        decorator.add(DropMissingValues())
    elif method not in ['mean', 'median', 'mode', 'constant']:
        raise ValueError("Method must be either 'mean', 'median','mode' or 'constant'")
    else:
        decorator.add(FillMissingValues(method=method,fill_value=fill_value))
    # Apply the decorator to the DataFrame
    return decorator.handle(df)