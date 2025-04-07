from zenml import step
import pandas as pd
from src.data_ingester.data_ingester_factory import DataIngesterFactory

@step
def data_ingestion_step(file_path: str, file_extension: str) -> pd.DataFrame:

    """
    Ingest data from certain file
    """

    data_ingestor = DataIngesterFactory.get_data_ingester(file_extension)
    df = data_ingestor.ingest(file_path=file_path)

    return df