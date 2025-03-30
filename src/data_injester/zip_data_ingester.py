from zipfile import ZipFile
from .abs_data_ingester import DataIngester
import pandas as pd
import os

EXTRACTED_PATH = "data/extracted"

"""
This class determines the zip data ingest
"""
class ZipDataIngester(DataIngester):
    def ingest(self, file_path: str) -> pd.DataFrame:
        # if the path is not determined zip file put a guard clause
        if not file_path.endswith('zip'):
            raise ValueError(".zip file should be provided!")
        
        # Extract zip file
        with ZipFile(file_path) as zip_file:
            print("ddd")
            zip_file.extractall(EXTRACTED_PATH)

        # list all files to check csv is there
        all_files = os.listdir(EXTRACTED_PATH)
        csv_files = [file for file in all_files if file.endswith('.csv')]
        print(csv_files)

        # if no CSV files found
        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV files found!")
        
        # if multiple files found
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files")
        
        #read the csv file
        df = pd.read_csv(os.path.join(EXTRACTED_PATH, csv_files[0]))
        return df

