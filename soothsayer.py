import click
from app import application


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-p",
    "--path_to_csv_file",
    type=str,
    required=True,
    help="Full path to the CSV file containing the data",
)
@click.option(
    "-n",
    "--num_rows",
    type=int,
    required=True,
    help="Number of rows to generate",
)
def generate(path_to_csv_file, num_rows):
    """Generate synthetic data from a CSV file"""
    print("Generating synthetic data from " + path_to_csv_file)
    application.generate_from_tabular(path_to_csv_file, num_rows)
    print("Done")
