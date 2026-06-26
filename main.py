import pandas as pd
from pathlib import Path
import pydicom


def extract_metadata(dataset):
    """
    Extract important metadata fields from a DICOM dataset.
    """

    metadata = {
        "Patient Name": str(getattr(dataset, "PatientName", "Not Available")),
        "Patient ID": str(getattr(dataset, "PatientID", "Not Available")),
        "Modality": str(getattr(dataset, "Modality", "Not Available")),
        "Study Date": str(getattr(dataset, "StudyDate", "Not Available")),
        "Manufacturer": str(getattr(dataset, "Manufacturer", "Not Available")),
    }
    return metadata

# Path to input folder
input_folder = Path("input")

# Store metadata of all DICOM files
all_metadata = []

# Process every DICOM file
for dicom_file in input_folder.glob("*.dcm"):

    print(f"Reading: {dicom_file.name}")

    dataset = pydicom.dcmread(dicom_file)

    metadata = extract_metadata(dataset)

    all_metadata.append(metadata)

print("\nAll Metadata:")

for metadata in all_metadata:
    print(metadata)

print("\nCreating DataFrame...")

df = pd.DataFrame(all_metadata)

print(df)

# Create output folder if it doesn't exist
output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

# Export to CSV
csv_file = output_folder / "dicom_metadata.csv"

df.to_csv(csv_file, index=False)

print(f"\nCSV file saved to: {csv_file}")

# Export to Excel
excel_file = output_folder / "dicom_metadata.xlsx"

df.to_excel(excel_file, index=False)

print(f"Excel file saved to: {excel_file}")