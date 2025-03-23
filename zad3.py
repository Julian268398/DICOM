
import pydicom

def dcm_tag_finder(dcm_path, *tags):
    file = pydicom.dcmread(dcm_path)
    for tag in tags:
        value = getattr(file, tag, "You're trying to get information that doesn't exists")
        print(f"{tag}: {value}")

dcm_tag_finder('lung_ct.dcm', 'ImageType', 'ImageOrientationPatient', 'SliceThickness')