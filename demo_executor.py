from src.framework.project import Project

if __name__ == "__main__":
    project = Project("prices_predictor_pipeline")

    project.file_path = "/home/dronelab/Projects/e2e-ml-flow/data/archive.zip"
    project.file_extension = ".zip"
    project.add_clean_data_method('drop', None)

    project.run_my_pipeline()