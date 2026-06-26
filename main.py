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

def main():
    # Path to input folder
    input_folder = Path("input")

    # Store metadata of all DICOM files
    all_metadata = []

    # Process every DICOM file
    successful_files = 0
    failed_files = 0

    for dicom_file in input_folder.glob("*.dcm"):

        print(f"Reading: {dicom_file.name}")

        try:
            dataset = pydicom.dcmread(dicom_file)

            metadata = extract_metadata(dataset)

            all_metadata.append(metadata)

            successful_files += 1

        except Exception as error:

            print(f"Error reading {dicom_file.name}: {error}")

            failed_files += 1

    print("\nProcessing Summary")
    print("------------------")
    print(f"Successful files : {successful_files}")
    print(f"Failed files     : {failed_files}")

    if not all_metadata:
        print("\nNo valid DICOM metadata found.")
        return

    print("\nAll Metadata:")
    print("------------")

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

if __name__ == "__main__":
    main()