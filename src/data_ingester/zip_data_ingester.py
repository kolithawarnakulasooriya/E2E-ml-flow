from zipfile import ZipFile
from .abs_data_ingester import DataIngester
import pandas as pd
import os

EXTRACTED_PATH = "data/extracted"

"""
Data Ingester for Zip type of classes
"""
class ZipDataIngester(DataIngester):

    """
    Ingest data from a certain zip file and read csv tabular data inside the file. return it as a pandas dataframe

    Parameters: file path string 

    Returns:
        pandas data frame 
    """
    def ingest(self, file_path: str) -> pd.DataFrame:
        # if the path is not determined zip file put a guard clause
        if not file_path.endswith('zip'):
            raise ValueError(".zip file should be provided!")
        
        # Extract zip file
        with ZipFile(file_path) as zip_file:
            zip_file.extractall(EXTRACTED_PATH)

        # list all files to check csv is there
        all_files = os.listdir(EXTRACTED_PATH)
        csv_files = [file for file in all_files if file.endswith('.csv')]

        # if no CSV files found
        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV files found!")
        
        # if multiple files found
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files")
        
        #read the csv file
        df = pd.read_csv(os.path.join(EXTRACTED_PATH, csv_files[0]))
        return df

