from zenml import step, pipeline
from src.steps.data_ingestion_step import data_ingestion_step
from src.steps.data_cleaning_step import data_clean_and_fix
from src.steps.feature_engineering_step import feature_engineering_step
from src.steps.outlier_handling_step import outlier_handling_step
from src.steps.data_splitting_step import data_splitting_step

@pipeline(name="prices_predictor_pipeline")
def my_pipeline():
    df = data_ingestion_step("data/archive.zip", ".zip")
    df = data_clean_and_fix(df, "drop", None)
    df = feature_engineering_step(df, "log", ["area"])
    df = feature_engineering_step(df, "standard", ["price"])
    df = outlier_handling_step(df, "remove", "zscore", 1.0)

    X_train, y_train, X_test, y_test = data_splitting_step(df, "basic", "price", 0.2, 1.0)

if __name__ == "__main__":
    my_pipeline()
