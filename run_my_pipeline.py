from src.pipelines import training_pipeline
import click

@click.command()
def main():
    """
    Run the training pipeline.
    """
    # Call the pipeline function
    training_pipeline.my_pipeline()
if __name__ == "__main__":
    main()
