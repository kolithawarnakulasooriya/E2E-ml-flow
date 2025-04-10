from typing import Optional
from abc import ABC

class Step(ABC):
    """Abstract base class for all steps in the pipeline."""
    def __init__(self, step_type: str,  parameters: Optional[dict] = None):
        """
        Base step class for all steps in the pipeline.
        Args:
            step_type (str): type of the step such as "data_ingestion", "data_cleaning"
            parameters (dict): parameters for the step
        """
        self._type = step_type

    @property
    def step_type(self):
        """Get the step type"""
        return self._type
    
class DataIngestionStep(Step):
    """Data Ingestion step class
    Args:
        file_path (str): path to the file
        file_extension (str): file extension
    """
    def __init__(self):
        super().__init__(step_type="data_ingestion")
    
    def set_parameters(self, file_path: str, file_extension: str):
        """Set the parameters for the step
        Args:
            file_path (str): path to the file
            file_extension (str): file extension
        """
        self._file_path = file_path
        self._file_extension = file_extension

    @property
    def file_path(self) -> str:
        """Get the file path"""
        return self._file_path
    
    @property
    def file_extension(self) -> str:
        """Get the file extension"""
        return self._file_extension
    
class DataCleaningStep(Step):
    """Data Cleaning step class
    """
    def __init__(self):
        super().__init__(step_type="data_cleaning")
    
    def set_parameters(self, method: str = 'drop', fill_value: Optional[int]=None):
        """Set the parameters for the step
        Args:
            method (str): method to handle missing values
            fill_value (int): value to fill missing values with
        """
        self._method = method
        self._fill_value = fill_value

    @property
    def method(self) -> str:
        """Get the file path"""
        return self._method
    
    @property
    def fill_value(self) -> Optional[int]:
        """Get the file extension"""
        return self._fill_value
    

class StepFactory():
    @staticmethod
    def create_step(step_type: str, **kwargs) -> Step:
        """Create a step object
        Args:
            step_type (str): type of the step such as "data_ingestion", "data_cleaning"
            kwargs: parameters for the step
        """
        if step_type == "data_ingestion":
            step = DataIngestionStep()
            step.set_parameters(kwargs.get("file_path"), kwargs.get("file_extension"))
            return step
        elif step_type == "data_cleaning":
            step = DataCleaningStep()
            step.set_parameters(kwargs.get("method"), kwargs.get("fill_value"))
            return step
        
        # Add more steps here as needed
        raise ValueError(f"Unknown step type: {step_type}")