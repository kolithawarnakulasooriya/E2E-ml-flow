from zenml import step, pipeline
from src.steps.data_ingestion_step import data_ingestion_step
from src.steps.data_cleaning_step import data_clean_and_fix

@pipeline(name="prices_predictor_pipeline")
def my_pipeline():
    df = data_ingestion_step("data/archive.zip", ".zip")
    df = data_clean_and_fix(df, "drop", None)


if __name__ == "__main__":
    my_pipeline()
