# https://how.dev/answers/how-to-create-a-video-from-images-in-python

import os
import cv2
import pydicom

def dcm_to_video(folder, video_filename, fps=10):

    valid_images = sorted([i for i in os.listdir(folder) if i.endswith(".dcm")])

    if not valid_images:
        print("Brak plików DICOM w folderze:", folder)
        return

    first_dcm = pydicom.dcmread(os.path.join(folder, valid_images[0]))
    first_image = first_dcm.pixel_array

    first_image = cv2.normalize(first_image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    h, w = first_image.shape
    size = (w, h)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_filename, fourcc, fps, size, isColor=False)

    for filename in valid_images:
        dcm_path = os.path.join(folder, filename)
        ds = pydicom.dcmread(dcm_path)
        img = ds.pixel_array
        img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

        out.write(img)

    out.release()
    print(f"Wideo zapisane jako: {video_filename}")


dcm_to_video('DICOM_Library', 'video_dicom_library.mp4', fps=10)
