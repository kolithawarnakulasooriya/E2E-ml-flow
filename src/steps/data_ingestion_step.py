from zenml import step
import pandas as pd
from src.core.data_ingesting import DataIngestFactory

@step
def data_ingestion_step(file_path: str, file_extension: str) -> pd.DataFrame:

    """
    Ingest data from certain file
    """

    data_ingest = DataIngestFactory.get_data_ingest(file_extension)
    df = data_ingest.ingest(file_path=file_path)

    return df