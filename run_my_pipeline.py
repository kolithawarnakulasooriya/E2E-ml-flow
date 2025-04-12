from src.pipelines.training_pipeline import train
import click

@click.command()
def main():
    """
    Run the training pipeline.
    """
    # Call the pipeline function
    train()
if __name__ == "__main__":
    main()
