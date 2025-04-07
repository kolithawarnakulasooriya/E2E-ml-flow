from src.framework.project import DefaultProjectTemplete

class Project(DefaultProjectTemplete):
    """Project Tempalate class
    Args:
        pipeline_name (str): name of the pipeline
    """
    def __init__(self, pipeline_name: str):
        super().__init__(pipeline_name)

if __name__ == "__main__":
    
    project = Project("prices_predictor_pipeline")

    project.file_path = "/home/dronelab/Projects/e2e-ml-flow/data/archive.zip"
    project.file_extension = ".zip"
    project.add_clean_data_method('drop', None)

    project.run_my_pipeline()