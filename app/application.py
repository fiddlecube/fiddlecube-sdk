import os
import sys
from sdv.datasets.local import load_csvs
from sdv.metadata import SingleTableMetadata
from sdv.lite import SingleTablePreset
from sdv.evaluation.single_table import evaluate_quality


def generate_from_tabular(path_to_csv_file, num_rows):
    folder_name = os.path.dirname(path_to_csv_file)
    datasets = load_csvs(folder_name=folder_name)

    filename = os.path.basename(path_to_csv_file)
    dataset_name = os.path.splitext(filename)[0]
    # the data is available under the file name
    csic_data = datasets[dataset_name]

    metadata = SingleTableMetadata()
    print("Detecting the metadata...")
    metadata.detect_from_csv(path_to_csv_file)
    print("Metadata detected:")
    print(metadata.to_dict())
    print()

    print("Training the model...")
    synthesizer = SingleTablePreset(metadata, "FAST_ML")
    synthesizer.fit(csic_data)

    print("Generating synthetic data...")
    synthetic_data = synthesizer.sample(num_rows=num_rows)
    synthetic_data.to_csv("synthetic_data.csv", index=False)
    print("Wrote synthetic data to synthetic_data.csv")

    quality_report = evaluate_quality(
        real_data=csic_data, synthetic_data=synthetic_data, metadata=metadata
    )
