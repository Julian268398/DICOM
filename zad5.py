# https://www.kaggle.com/code/neuerfrhling/read-ct-dicom
# https://stackoverflow.com/questions/34782409/understanding-dicom-image-attributes-to-get-axial-coronal-sagittal-cuts + poprawka chatu

import os
import pydicom
import numpy as np
import matplotlib.pyplot as plt

# dicom_data = pydicom.dcmread('ct_brain.dcm')
# image = dicom_data.pixel_array
# plt.imshow(image, cmap='bone')
# plt.colorbar()
# plt.title("DICOM Image")
# plt.show()


def detect_orientation(dicom_file):
    ds = pydicom.dcmread(dicom_file)

    orientation = ds.ImageOrientationPatient

    # Sprawdzamy orientację na podstawie znanych wartości
    if orientation == [1, 0, 0, 0, 0, -1]:
        return "coronal"
    elif orientation == [0, 1, 0, 0, 0, -1]:
        return "sagittal"
    elif orientation == [1, 0, 0, 0, 1, 0]:
        return "axial"
    else:
        return "unknown"


def chose_dcm_face(folder_path, face, coordinate):
    valid_images = sorted([os.path.join(folder_path, i) for i in os.listdir(folder_path) if i.endswith(".dcm")])

    if not valid_images:
        print("No DICOM data in this directory:", folder_path)
        return

    # Wykrywamy orientację stosu na podstawie pierwszego obrazu
    detected_orientation = detect_orientation(valid_images[0])
    print(f"Detected orientation: {detected_orientation}")

    matrix_3d = [pydicom.dcmread(image).pixel_array for image in valid_images]
    matrix_3d = np.array(matrix_3d)

    # Jeśli wykryta orientacja różni się od użytkownika, zmieniamy osie
    if detected_orientation == "coronal":
        matrix_3d = np.transpose(matrix_3d, (1, 0, 2))  # Zamiana (Z, Y, X) → (Y, Z, X)
    elif detected_orientation == "sagittal":
        matrix_3d = np.transpose(matrix_3d, (2, 0, 1))  # Zamiana (Z, Y, X) → (X, Z, Y)

    z_dim, y_dim, x_dim = matrix_3d.shape

    if face == 'axial':
        if not (0 <= coordinate < z_dim):
            return "Coordinate that you provided is out of range!"
        slice_2d = matrix_3d[coordinate, :, :]

    elif face == 'coronal':
        if not (0 <= coordinate < y_dim):
            return "Coordinate that you provided is out of range!"
        slice_2d = matrix_3d[:, coordinate, :]

    elif face == 'sagittal':
        if not (0 <= coordinate < x_dim):
            return "Coordinate that you provided is out of range!"
        slice_2d = matrix_3d[:, :, coordinate]

    else:
        print("Invalid face option! Use 'axial', 'coronal', or 'sagittal'.")
        return

    plt.imshow(slice_2d, cmap="gray")
    plt.title(f"{face.capitalize()} Slice at {coordinate}")
    plt.axis("off")
    plt.show()


# Przykład użycia
chose_dcm_face("DICOM_Library", "sagittal", 150)