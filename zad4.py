# https://pydicom.github.io/pydicom/dev/tutorials/dataset_basics.html
# https://pydicom.github.io/pydicom/stable/guides/user/working_with_pixel_data.html?utm_source=chatgpt.com

import pydicom
import numpy as np


# metadata modification
name = 'lung_ct.dcm'
file = pydicom.dcmread(name)  # Otwieranie pliku
elem = file[0x0008, 0x0060]
file.Modality = 'MRI'
print(elem)

# picture modification - negativ invertion
arr = file.pixel_array
arr = np.max(arr) - arr
file.PixelData = arr.astype(file.pixel_array.dtype).tobytes()

# saving file
file.save_as(f'{name.removesuffix(".dcm")}_modified.dcm')
