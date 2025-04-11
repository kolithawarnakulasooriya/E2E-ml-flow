from zenml import step
from src.core.model_evaluating import ModelEvaluatorFactory
from sklearn.pipeline import Pipeline
import pandas as pd
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@step
def model_evaluator_step(model: Pipeline, X_test: pd.DataFrame, y_test:pd.DataFrame) -> tuple[float, float]:
    """
    Evaluate the model using the provided test data.

    Args:
        model: The model to be evaluated.
        X_test: The features of the test data.
        y_test: The target variable of the test data.

    Returns:
        The evaluation result.
    """
    logging.info("Starting model evaluation.")
    # Preprocess the test data if necessary
    
    X_test_processed = model.named_steps['preprocessor'].transform(X_test)

    # Create a model evaluator instance
    evaluator = ModelEvaluatorFactory.create_model_evaluator("basic")
    
    evaluation_result = evaluator.evaluate(model.named_steps['model'], X_test_processed, y_test)
    logging.info("Model evaluation completed.")

    return evaluation_result.get('mse'), evaluation_result.get('r2')