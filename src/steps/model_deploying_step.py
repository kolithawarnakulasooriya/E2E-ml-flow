from zenml import pipeline, step, get_step_context
from zenml.client import Client
from mlflow.tracking import MlflowClient, artifact_utils
from sklearn.pipeline import Pipeline
from typing import Optional, cast
from zenml.integrations.mlflow.services import MLFlowDeploymentService
from zenml.integrations.mlflow.services import MLFlowDeploymentConfig
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import MLFlowModelDeployer

import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@step
def model_deployment_step(name:str, description:str, run_id:str, model: Pipeline, workers:int = 1) -> Optional[MLFlowDeploymentService]:

    logging.info("Starting model deployment step...")
    logging.info(f"Run ID: {run_id}")

    client = Client()
    experiment_tracker = client.active_stack.experiment_tracker
    experiment_tracker.configure_mlflow()

    client = MlflowClient()
    model_name = model.named_steps['model'].__class__.__name__

    model_uri = artifact_utils.get_artifact_uri(
        run_id=run_id, artifact_path=model_name
    )

    model_deployer = cast(
        MLFlowModelDeployer, MLFlowModelDeployer.get_active_model_deployer()
    )

    logging.info(f"Model URI: {model_uri}, Model Name: {model_name}")

    mlflow_deployment_config = MLFlowDeploymentConfig(
        name = name,
        description = description,
        pipeline_name = get_step_context().pipeline.name,
        pipeline_step_name = get_step_context().step_name,
        model_uri = model_uri,
        model_name = model_name,
        workers = workers,
    )

    predictor_cfg = MLFlowDeploymentConfig(
        model_name=model_name or "",
        model_uri=model_uri,
        workers= workers,
        pipeline_name=get_step_context().pipeline.name,
        pipeline_step_name=get_step_context().step_name,
    )

    # Fetch existing services with same pipeline name, step name and model name
    existing_services = model_deployer.find_model_server(
        config=predictor_cfg.model_dump(),
    )

    logging.info(f"Stopping existing services... {existing_services}")
    for existing_service in existing_services:
        existing_service.stop()

    service = model_deployer.deploy_model(
        config=mlflow_deployment_config, 
        service_type=MLFlowDeploymentService.SERVICE_TYPE
    )

    logging.info(f"The deployed service info: {model_deployer.get_model_server_info(service)}")
    
    return service