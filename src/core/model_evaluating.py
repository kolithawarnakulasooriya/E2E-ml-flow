from abc import ABC, abstractmethod
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ModelEvaluatorStrategy(ABC):
    """
    Abstract base class for model evaluation strategies.
    """

    @abstractmethod
    def evaluate(self, model, x_test: pd.DataFrame, y_test:pd.Series) -> dict:
        """
        Evaluate the model using the provided data.

        Args:
            model: The model to be evaluated.
            x_test: The features of the test data.
            y_test: The target variable of the test data.

        Returns:
            The evaluation result.
        """
        pass
    
class BasicModalEvolutionStrategy(ModelEvaluatorStrategy):
    """
    Basic model evaluation strategy.
    """

    def evaluate(self, model, x_test: pd.DataFrame, y_test:pd.Series):
        """
        Evaluate the model using the provided data.

        Args:
            model: The model to be evaluated.
            x_test: The features of the test data.
            y_test: The target variable of the test data.

        Returns:
            The evaluation result.
        """
        logging.info("Evaluating model using basic evaluation strategy.")
        
        y_pred = model.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        logging.info(f"Mean Squared Error: {mse}")
        logging.info(f"R^2 Score: {r2}")
        return {
            "mse": mse,
            "r2": r2
        }
        
class ModelEvaluatorFactory:
    """
    Factory class to create model evaluator instances.
    """

    @staticmethod
    def create_model_evaluator(strategy: str) -> ModelEvaluatorStrategy:
        """
        Get a model evaluator instance based on the strategy.

        Args:
            strategy: The strategy to be used for evaluation.

        Returns:
            An instance of the model evaluator.
        """
        if strategy == "basic":
            return BasicModalEvolutionStrategy()
        else:
            raise ValueError(f"Unknown evaluation strategy: {strategy}")