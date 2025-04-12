from zenml import step, Model, ArtifactConfig
from zenml.client import Client
from sklearn.pipeline import Pipeline
from typing import Annotated
import mlflow
from mlflow.models import infer_signature
from src.core.model_building import ModelBuildFactory
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

tracker = Client().active_stack.experiment_tracker.name
model = Model(
        name="prediction_model_v001",
        description="Version 001",
        version=None,
        license="Apache-2.0",
    )

@step(enable_cache=False,model=model, experiment_tracker=tracker)
def model_building_step(strategy: str, X_train: pd.DataFrame, y_train: pd.DataFrame) -> tuple[Annotated[Pipeline, ArtifactConfig(name="model_pipeline", is_artifact=True)], str]:
    """
    Step to build and train a model.

    Parameters:
    X_train (pd.DataFrame): The features for training.
    y_train (pd.Series): The target variable for training.
    
    Returns:
    model: The trained model.
    """
    
    model_builder = ModelBuildFactory.create_model_strategy(strategy)
    model_builder.set_training_data(X_train, y_train)
    model_builder.build_model()
    
    try:
        if model_builder.model_pipeline is None:
            raise ValueError("Model pipeline is not built.")
            
        mlflow.autolog()

        if mlflow.active_run() is None:
            mlflow.end_run()
            mlflow.start_run()
            logging.info("Starting MLflow run...")

        with mlflow.active_run() as run:
            model_builder.fit()
            run_id = run.info.run_id
            logging.info(f"Model training completed. Run ID: {run.info.run_id}")

            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="sklearn-model",
                registered_model_name="sk-learn-random-forest-reg-model",
            )

    except Exception as e:
        print(f"Error during model training: {e}")
        raise
    finally:
        mlflow.end_run()
    
    return model_builder.get_pipeline(), run_id