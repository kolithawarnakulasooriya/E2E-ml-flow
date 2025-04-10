from zenml import step, pipeline
from src.steps.data_ingestion_step import data_ingestion_step
from src.steps.data_cleaning_step import data_clean_and_fix
from src.steps.feature_engineering_step import feature_engineering_step

@pipeline(name="prices_predictor_pipeline")
def my_pipeline():
    df = data_ingestion_step("data/archive.zip", ".zip")
    df = data_clean_and_fix(df, "drop", None)
    df = feature_engineering_step(df, "log", ["price", "area"])

if __name__ == "__main__":
    my_pipeline()
