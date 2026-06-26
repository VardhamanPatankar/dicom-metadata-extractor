from pathlib import Path

import pydicom


def extract_metadata(dataset):
    """
    Extract important metadata fields from a DICOM dataset.
    """

    metadata = {
        "Patient Name": getattr(dataset, "PatientName", "Not Available"),
        "Patient ID": getattr(dataset, "PatientID", "Not Available"),
        "Modality": getattr(dataset, "Modality", "Not Available"),
        "Study Date": getattr(dataset, "StudyDate", "Not Available"),
        "Manufacturer": getattr(dataset, "Manufacturer", "Not Available"),
    }

    return metadata


# Path to input folder
input_folder = Path("input")

# Path to the DICOM file
dicom_file = input_folder / "CT_small.dcm"

# Read DICOM file
dataset = pydicom.dcmread(dicom_file)

# Extract metadata
metadata = extract_metadata(dataset)

print(metadata)