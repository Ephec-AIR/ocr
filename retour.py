from fonctions import *
from PIL import Image
import pytesseract

import numpy as np
import matplotlib.pyplot as plt
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

matrix_compteur = clean_image("numbers//electricity.jpg")


#print(pytesseract.image_to_string(Image.fromarray(matrix_compteur), config=tessdata_dir_config))

compteur = np.array(clean_image("numbers//electricity.jpg"))
template = np.array(clean_image("numbers//template.jpg"))
matrix_compteur_edge = match_template(compteur, template)


