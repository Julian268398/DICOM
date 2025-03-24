# https://pydicom.github.io/pydicom/dev/tutorials/dataset_basics.html
# https://stackoverflow.com/questions/66697978/how-to-replace-an-image-in-dicom-in-python

import pydicom


# metadata modification
name = '12.dcm'
file = pydicom.dcmread(name)  # Otwieranie pliku
elem = file[0x0008,0x0060]
file.Modality = 'MRI'
print(elem)

# picture modification
png = Image.fromarray(file.pixel_array)

# saving file
# file.save_as(f'{name}_modified.dcm')
