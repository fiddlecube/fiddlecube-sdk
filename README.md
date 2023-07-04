# Soothsayer - Generate synthetic tabular data
Soothsayer enables the generation of synthetic tabular data.

## Steps
1. Move the CSV files that you want to augment to the `data/` folder
2. Run the following commands:
```
pipenv shell
python main.py [CSV file name] [number of rows to generate]
```
Example:
```
python main.py csic_ecml_1000 10000
```

You will find the synthetic data in the `output/` folder.