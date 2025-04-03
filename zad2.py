# https://medium.com/@ashkanpakzad/reading-editing-dicom-metadata-w-python-8204223a59f6
import pydicom
def dcm_metadata(dcm_path):
    file = pydicom.dcmread(dcm_path)  # Otwieranie pliku
    print(file)
    return file

dcm_metadata('DICOM_Library/1-003.dcm')