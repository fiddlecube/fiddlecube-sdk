from sdv.datasets.local import load_csvs
from sdv.metadata import SingleTableMetadata
from sdv.lite import SingleTablePreset
from sdv.evaluation.single_table import evaluate_quality

# assume that my_folder contains 1 CSV file named 'guests.csv'
datasets = load_csvs(folder_name='data/')

# the data is available under the file name
csic_data = datasets['csic_ecml_1000']

metadata = SingleTableMetadata()
print('Detecting the metadata...')
metadata.detect_from_csv(filepath='data/csic_ecml_1000.csv')
print('Metadata detected:')
print(metadata.to_dict())

print('Training the model...')
synthesizer = SingleTablePreset(metadata, 'FAST_ML')
synthesizer.fit(csic_data)

print('Generating synthetic data...')
synthetic_data = synthesizer.sample(num_rows=10000)
synthetic_data.to_csv('output/synthetic_data.csv', index=False)

quality_report = evaluate_quality(
    real_data=csic_data, synthetic_data=synthetic_data, metadata=metadata)

# if __name__ == "__main__":
#     main()