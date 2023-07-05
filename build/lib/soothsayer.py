import click
from app import application

@click.group()
def cli():
    pass

@cli.command()
@click.option('-p', '--path_to_csv_file', type=str, help='Full path to the CSV file containing the data')
def generate(path_to_csv_file):
    """Generate synthetic data from a CSV file"""
    print('Generating synthetic data from ' + path_to_csv_file)
    application.generate_from_tabular(path_to_csv_file)
    print('Done')
