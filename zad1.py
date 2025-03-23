# information sources:
# Dicom files that I used comes from portal kaggle.
# How to read dicom data: https://www.kaggle.com/code/neuerfrhling/read-ct-dicom

import pydicom
import numpy as np

def dcm_shape(dcm_path):
    file = pydicom.dcmread(dcm_path) # Otwieranie pliku
    pixel_array = file.pixel_array
    return pixel_array.shape

print(dcm_shape('lung_ct.dcm'))
print(dcm_shape('spine_mri.dcm'))
print(dcm_shape('ct_brain.dcm'))