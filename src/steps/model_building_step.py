from zenml import step, Model, ArtifactConfig
from zenml.client import Client
from sklearn.pipeline import Pipeline
from typing import Annotated
import mlflow
from src.core.model_building import ModelBuildFactory
import pandas as pd


model = Model(
        name="prediction_model_v001",
        description="Version 001",
        version=None,
        license="Apache-2.0",
    )

@step(enable_cache=False,model=model)
def model_building_step(strategy: str, X_train: pd.DataFrame, y_train: pd.DataFrame) -> Annotated[Pipeline, ArtifactConfig(name="model_pipeline", is_artifact=True)]:
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
        
        if not mlflow.active_run():
            mlflow.start_run()
            
        mlflow.autolog()
        
        model_builder.fit()
    except Exception as e:
        print(f"Error during model training: {e}")
        raise
    finally:
        if mlflow.active_run():
            mlflow.end_run()
    
    return model_builder.get_pipeline()