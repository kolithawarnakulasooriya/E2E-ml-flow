from src.framework.project import DefaultProjectTemplete
from src.framework.pipeline_step import StepFactory

if __name__ == "__main__":
    
    project = DefaultProjectTemplete("prices_predictor_pipeline")
    project.add_step(StepFactory.create_step("data_ingestion", file_path="data/archive.zip", file_extension=".zip"))
    project.add_step(StepFactory.create_step("data_cleaning", method="drop", fill_value=None))

    project.run_pipeline()