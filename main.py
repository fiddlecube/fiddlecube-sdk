import sys
from sdv.datasets.local import load_csvs
from sdv.metadata import SingleTableMetadata
from sdv.lite import SingleTablePreset
from sdv.evaluation.single_table import evaluate_quality

def main(dataset_name):
    # assume that my_folder contains 1 CSV file named 'guests.csv'
    datasets = load_csvs(folder_name='data/')

    # the data is available under the file name
    csic_data = datasets[dataset_name]

    metadata = SingleTableMetadata()
    print('Detecting the metadata...')
    metadata.detect_from_csv(filepath='data/' + dataset_name + '.csv')
    print('Metadata detected:')
    print(metadata.to_dict())
    print()

    print('Training the model...')
    synthesizer = SingleTablePreset(metadata, 'FAST_ML')
    synthesizer.fit(csic_data)

    print('Generating synthetic data...')
    synthetic_data = synthesizer.sample(num_rows=10000)
    synthetic_data.to_csv('output/synthetic_data.csv', index=False)
    print('Wrote synthetic data to output/synthetic_data.csv')

    quality_report = evaluate_quality(
        real_data=csic_data, synthetic_data=synthetic_data, metadata=metadata)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: missing arguments")
        print("Usage: python main.py [dataset_name] [target_rows]")
        print("Example: python main.py csic_ecml_1000 10000")
        exit(1)
    main(sys.argv[1])