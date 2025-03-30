from .abs_data_ingester import DataIngester
from .zip_data_ingester import ZipDataIngester

class DataIngesterFactory():

    @staticmethod
    def get_data_ingester(file_extension: str) -> DataIngester:
        
        match(file_extension):
            case 'zip':
                return ZipDataIngester()
            
        raise ValueError("No accepted ingester found!")