#https://www.youtube.com/watch?v=k6hD0xNp2B8&list=PLQCkKRar9trMY2qJAU6H4nZQwTfZc91Oq
import numpy as np
import pydicom
from PIL import Image

def dcm_to_jpg(path):
    pic = pydicom.dcmread(path)
    pic = pic.pixel_array.astype(float)
    rescaled_pic = (np.maximum(pic, 0.0)/pic.max())*255
    final = np.uint8(rescaled_pic)
    final = Image.fromarray(final)
    final.show()
    final.save(f'{path.removesuffix(".dcm")}.jpg')


dcm_to_jpg('1-003.dcm')
