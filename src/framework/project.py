from typing import List, Optional
from zenml import pipeline, Model, step
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from src.steps.data_ingestion_step import data_ingestion_step
from src.steps.data_cleaning_step import data_clean_and_fix
from abc import abstractmethod

class Clean_Data_Method:
    """clean data method class
    Args:
        method (str): clean data method
        fill_value (int): fill value for the method
    """
    def __init__(self, method, fill_value):
        self.method:str = method
        self.fill_value:Optional[int] = fill_value

class DefaultProjectTemplete():
    """Project Tempalate class
    Args:
        pipeline_name (str): name of the pipeline
    """
    def __init__(self, pipeline_name: str):
        self._pipeline_name:str = pipeline_name
        self._file_path:str = None
        self._file_extension:str = None
        self._clean_data_methods : List[Clean_Data_Method] = []

    @property
    def pipeline_name(self):
        """Get the pipeline name"""
        return self.pipeline_name
    
    @pipeline_name.setter
    def pipeline_name(self, name):
        """Set the pipeline name"""
        self._pipeline_name = name
    
    @property
    def file_path(self):
        """Get the file path"""
        return self._file_path
    
    @file_path.setter
    def file_path(self, path):
        """Set the file path"""
        if not path:
            raise ValueError("File path cannot be empty")
        if not isinstance(path, str):
            raise ValueError("File path must be a string")
        self._file_path = path
        
    @property
    def file_extension(self):
        """Get the file extension"""
        return self._file_extension
    
    @file_extension.setter
    def file_extension(self, extension):
        """Set the file extension"""
        self._file_extension = extension
    
    @property
    def clean_data_methods(self):
        """Get the clean data methods"""
        return self._clean_data_methods
    
    @clean_data_methods.setter
    def clean_data_methods(self, methods):
        """Set the clean data methods"""
        self._clean_data_methods = methods
    
    def add_clean_data_method(self, method, fill_value):
        """Add a clean data method
        Args:
            method (str): clean data method
            fill_value (int): fill value for the method
        """
        self._clean_data_methods.append(Clean_Data_Method(method, fill_value))
    
    @abstractmethod
    def training_pipeline(self):
        """Training pipeline
        """
        data_frame = data_ingestion_step(self._file_path, self._file_extension)
        
        for clean_data_method in self._clean_data_methods:
            data_frame = data_clean_and_fix(data_frame, clean_data_method.method, clean_data_method.fill_value)
         
    def run_my_pipeline(self):
        """Run the pipeline"""
        
        @pipeline(name="pipeline_name")
        def training_pipeline_call():
            self.training_pipeline()

        training_pipeline_call()
        
    def print(self):
        print(f"Project Name: {self._model_name}")
        print(f"File Path: {self._file_path}")
        print(f"File Extension: {self._file_extension}")
        print(f"Clean Data Methods: {[method.method for method in self._clean_data_methods]}")
        print(f"mlflow ui --backend-store-uri '{get_tracking_uri()}'")