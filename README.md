# DICOM Metadata Extraction Utility

## Project Overview
This project is a Python-based utility that reads DICOM (Digital Imaging and Communications in Medicine) files, extracts important metadata fields, and exports the extracted information into both CSV and Excel formats.
The utility is designed to process one or more DICOM files placed inside the `input` folder while handling missing metadata fields and file-reading errors gracefully.

## Features
- Read one or multiple DICOM files from the `input` folder
- Extract key DICOM metadata fields
- Handle missing metadata safely
- Continue processing even if a DICOM file is corrupted or unreadable
- Generate CSV output
- Generate Excel output
- Display processing summary
- Create output directory automatically if it does not exist

## Metadata Extracted
The utility extracts the following metadata fields:
- Patient Name
- Patient ID
- Modality
- Study Date
- Manufacturer
- Institution Name
- Study Description
- Series Description
- Body Part Examined
- Rows
- Columns

## Technologies Used
- Python 3
- pydicom
- pandas
- openpyxl
- pathlib

## Project Structure
```
DicomMetadataExtractor/
│
├── input/
│   └── CT_small.dcm
│
├── output/
│   ├── dicom_metadata.csv
│   └── dicom_metadata.xlsx
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation
Clone the repository:

```bash
git clone https://github.com/VardhamanPatankar/dicom-metadata-extractor
```

Navigate to the project directory:

```bash
cd DicomMetadataExtractor
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.
**Windows**
```bash
.venv\Scripts\activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Place one or more DICOM files inside the `input` folder.
2. Run the program:
```bash
python main.py
```

3. The extracted metadata will be saved inside the `output` folder as:
- `dicom_metadata.csv`
- `dicom_metadata.xlsx`

## Error Handling
The utility includes the following error handling:
- Handles missing DICOM metadata fields using `getattr()`
- Continues processing if a DICOM file cannot be read
- Displays processing summary showing successful and failed files
- Detects missing `input` folder
- Handles permission errors while saving the Excel file (for example, if the file is already open)

## Sample Output
```
Reading: CT_small.dcm

Processing Summary
------------------
Successful files : 1
Failed files     : 0

CSV file saved to: output/dicom_metadata.csv
Excel file saved to: output/dicom_metadata.xlsx
```

## Future Enhancements
Possible future improvements include:
- Recursive folder scanning
- Command-line arguments for custom input/output paths
- Logging to a log file
- GUI interface using Tkinter or PyQt
- Additional DICOM metadata extraction
- Export to JSON format

## Author
Vardhaman Patankar
