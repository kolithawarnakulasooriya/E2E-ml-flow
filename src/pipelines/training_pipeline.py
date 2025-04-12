from zenml import pipeline
import pandas as pd
import numpy as np
from zenml import Model
from zenml.client import Client
from src.steps.data_ingestion_step import data_ingestion_step
from src.steps.data_cleaning_step import data_clean_and_fix
from src.steps.feature_engineering_step import feature_engineering_step
from src.steps.outlier_handling_step import outlier_handling_step
from src.steps.data_splitting_step import data_splitting_step
from src.steps.model_building_step import model_building_step
from src.steps.model_evaluator_step import model_evaluator_step
from src.steps.model_deploying_step import model_deployment_step

@pipeline(name="pipeline-v001", model=Model(name="prediction_model_v001"), enable_cache=False)
def train():
    df = pd.DataFrame()
    df = data_ingestion_step("data/archive.zip", ".zip", "dating_app_behavior_dataset.csv")
    df = data_clean_and_fix(df, "drop", None)
    df = feature_engineering_step(df, "custom", ['gender','sexual_orientation','likes_received','mutual_matches','message_sent_count','last_active_hour'])
    #df = feature_engineering_step(df, "numerical", None)
    df = feature_engineering_step(df, "log", ['likes_received','mutual_matches','message_sent_count','last_active_hour'])
    df = outlier_handling_step(df, "remove", "zscore", 1.0)
    
    X_train, X_test, y_train, y_test = data_splitting_step(df, "basic", "price", 0.2, 1.0)
    
    model,run_id = model_building_step("linear_regression", X_train, y_train)
    
    mse, r2 = model_evaluator_step(model, X_test, y_test)

    model_deployment_step(run_id, model)
    
    return model