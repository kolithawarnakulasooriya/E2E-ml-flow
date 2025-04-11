from zenml import pipeline
import pandas as pd
import numpy as np
from src.steps.data_ingestion_step import data_ingestion_step
from src.steps.data_cleaning_step import data_clean_and_fix
from src.steps.feature_engineering_step import feature_engineering_step
from src.steps.outlier_handling_step import outlier_handling_step
from src.steps.data_splitting_step import data_splitting_step
from src.steps.model_building_step import model_building_step
from src.steps.model_evaluator_step import model_evaluator_step

@pipeline(name="pipeline-v001")
def my_pipeline():
    df = pd.DataFrame()
    df = data_ingestion_step("data/archive.zip", ".zip")
    df = data_clean_and_fix(df, "drop", None)
    df = feature_engineering_step(df, "numerical", None)
    df = feature_engineering_step(df, "log", ["price"])
    df = outlier_handling_step(df, "remove", "zscore", 1.0)
    
    X_train, X_test, y_train, y_test = data_splitting_step(df, "basic", "price", 0.2, 1.0)
    
    model = model_building_step("linear_regression", X_train, y_train)
    
    mse, r2 = model_evaluator_step(model, X_test, y_test)
    
    return model