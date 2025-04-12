import pandas as pd
from abc import ABC, abstractmethod
from zipfile import ZipFile
import pandas as pd
import os

class DataIngest(ABC):
    """
        Abstract base class for data ingest
    """
    @abstractmethod
    def ingest(self, file_path:str) -> pd.DataFrame:
        """_Perform any data ingestion from any data source

        Args:
            file_path (str): specific filetype

        Returns:
            pd.DataFrame: return extracted dataframe
        """
        pass

EXTRACTED_PATH = "data/extracted"

"""
Data Ingest for Zip type of classes
"""
class ZipDataIngest(DataIngest):

    """
    Ingest data from a certain zip file and read csv tabular data inside the file. return it as a pandas dataframe

    Parameters: file path string 

    Returns:
        pandas data frame 
    """
    def ingest(self, file_path: str, exact_csv: str = None) -> pd.DataFrame:
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
        if exact_csv == None and len(csv_files) > 1:
            raise ValueError("Multiple CSV files")
        
        # if exact csv file find
        if exact_csv:
            csv_files = [file for file in csv_files if file == exact_csv]

            if not csv_files:
                raise ValueError("No Exact CSV found")
        
        #read the csv file
        df = pd.read_csv(os.path.join(EXTRACTED_PATH, csv_files[0]))
        return df
    
class DataIngestFactory():
    @staticmethod
    def get_data_ingest(file_extension: str) -> DataIngest:
        
        match(file_extension):
            case '.zip':
                return ZipDataIngest()
            
        raise ValueError("No accepted ingest found!")


