# https://www.kaggle.com/code/neuerfrhling/read-ct-dicom

import pydicom
import matplotlib.pyplot as plt

# dicom_data = pydicom.dcmread('ct_brain.dcm')
# image = dicom_data.pixel_array
# plt.imshow(image, cmap='bone')
# plt.colorbar()
# plt.title("DICOM Image")
# plt.show()


def visualize_slice(dicom_file, plane='axial', index=None):
    """
    Wizualizuje przekrój obrazu DICOM w wybranej płaszczyźnie.

    Parametry:
    - dicom_file: Ścieżka do pliku DICOM (lub już wczytany obiekt pydicom.Dataset)
    - plane: 'axial' (poprzeczny), 'coronal' (czołowy), 'sagittal' (strzałkowy)
    - index: Współrzędna przekroju (domyślnie środkowy przekrój)
    """

    # Jeśli użytkownik podał ścieżkę, wczytaj plik DICOM
    dicom_data = pydicom.dcmread(dicom_file)


    # Pobranie macierzy pikseli
    image_array = dicom_data.pixel_array

    # Sprawdzenie, czy obraz jest 3D
    if len(image_array.shape) == 2:
        print("Obraz jest 2D, nie można wyświetlić innych przekrojów.")
        plt.imshow(image_array, cmap='bone')
        plt.colorbar()
        plt.title("DICOM 2D Image")
        plt.show()
        return

    # Wymiary obrazu
    z_dim, y_dim, x_dim = image_array.shape  # (warstwy, wysokość, szerokość)

    # Wybór domyślnego indeksu (środkowy przekrój, jeśli nie podano)
    if index is None:
        if plane == 'axial':
            index = z_dim // 2
        elif plane == 'coronal':
            index = y_dim // 2
        elif plane == 'sagittal':
            index = x_dim // 2

    # Wybór odpowiedniego przekroju
    if plane == 'axial':  # Oś Z (poprzeczny)
        slice_img = image_array[index, :, :]
        title = f"Axial slice {index}"
    elif plane == 'coronal':  # Oś Y (czołowy)
        slice_img = image_array[:, index, :]
        title = f"Coronal slice {index}"
    elif plane == 'sagittal':  # Oś X (strzałkowy)
        slice_img = image_array[:, :, index]
        title = f"Sagittal slice {index}"
    else:
        raise ValueError("Nieprawidłowa płaszczyzna! Wybierz 'axial', 'coronal' lub 'sagittal'.")

    # Wizualizacja przekroju
    plt.imshow(slice_img, cmap='bone')
    plt.colorbar()
    plt.title(title)
    plt.show()


visualize_slice('1-1.dcm')