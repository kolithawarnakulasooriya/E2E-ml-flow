from zenml import step
import pandas as pd
from src.core.outlier_handling import OutlierHandler

@step
def outlier_handling_step(df: pd.DataFrame, handling_method:str, detection_method:str, extra: float = 0.0) -> pd.DataFrame:

    """
    Step to handle outliers in the given data.

    Parameters:
    df (pd.DataFrame): The input data.
    handling_method (str): The method to use for handling outliers ('remove' or 'replace').
    detection_method (str): The method to use for detecting outliers ('zscore' or 'iqr').
    extra (float): The extra parameters to use for the methods.

    Returns:
    pd.DataFrame: A DataFrame with outliers handled.
    """
    if df is None or not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input DataFrame is empty or None.")
    
    return OutlierHandler(method=detection_method, extra=extra).handle_outliers(method=handling_method, df=df)