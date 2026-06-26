import pydicom
from pydicom.data import get_testdata_file

# Get sample DICOM file
filename = get_testdata_file("CT_small.dcm")

# Read the DICOM file
dataset = pydicom.dcmread(filename)

print("Patient Name :", dataset.PatientName)
print("Patient ID   :", dataset.PatientID)
print("Modality     :", dataset.Modality)
print("Study Date   :", dataset.StudyDate)
print("Manufacturer :", dataset.Manufacturer)