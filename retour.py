from fonctions import *
from PIL import Image
import pytesseract

import numpy as np
import matplotlib.pyplot as plt
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

compteur2 = np.array(clean_image("numbers//electricity.jpg"))


compteur = np.array(clean_image("numbers//mini_compteur.png"))
template = np.array(clean_image("numbers//template.jpg"))


#img = cv2.imread(Image.fromarray(compteur),0)
edges = cv2.Canny(compteur,100,200)
edges2 = cv2.Canny(compteur2,100,200)
Image.fromarray(compteur).show()
Image.fromarray(compteur2).show()
Image.fromarray(edges).show()
print(pytesseract.image_to_string(Image.fromarray(compteur), config=tessdata_dir_config))
print(pytesseract.image_to_string(Image.fromarray(compteur2), config=tessdata_dir_config))
