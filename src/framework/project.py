from typing import List
import pandas as pd
from zenml import pipeline
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from .pipeline_step import Step
from src.steps.data_ingestion_step import data_ingestion_step
from src.steps.data_cleaning_step import data_clean_and_fix

class DefaultProjectTemplete():
    """Project Tempalate class
    Args:
        pipeline_name (str): name of the pipeline
    """
    def __init__(self, pipeline_name: str):
        self._pipeline_name:str = pipeline_name
        self._steps:List[Step] = []
        self._df: pd.DataFrame = pd.DataFrame()

    def get_pipeline_name(self):
        """Get the pipeline name"""
        return self.pipeline_name
    
    def add_step(self, step: Step):
        """Add a step to the pipeline
        Args:
            step (Step): step object
        """
        self._steps.append(step)

    def run_pipeline(self):
        """Run the pipeline"""
        @pipeline(name=self._pipeline_name)
        def pipeline_call():
            for step in self._steps:
                if step.step_type == "data_ingestion":
                    self._df = data_ingestion_step(step.file_path, step.file_extension)
                elif step.step_type == "data_cleaning":
                    self._df = data_clean_and_fix(self._df, step.method, step.fill_value)
                # Add more steps here as needed

        pipeline_call()
