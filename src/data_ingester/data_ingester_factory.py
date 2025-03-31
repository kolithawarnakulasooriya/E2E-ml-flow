from .abs_data_ingester import DataIngester
from .zip_data_ingester import ZipDataIngester

class DataIngesterFactory():

    """
    Return the extract ingester object for a certain file type

    Parameters:
        file_extension: pass the type of file. such as .csv, .zip

    Raises:
        ValueError: if no compatible file type found

    Returns:
        Corresponding DataIngester object 
    """
    @staticmethod
    def get_data_ingester(file_extension: str) -> DataIngester:
        
        match(file_extension):
            case '.zip':
                return ZipDataIngester()
            
        raise ValueError("No accepted ingester found!")