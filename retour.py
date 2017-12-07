from ocr import *
from PIL import Image
import pytesseract

import numpy as np
import matplotlib.pyplot as plt
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

matrix_compteur = clean_image("electricity.jpg")


#print(pytesseract.image_to_string(Image.fromarray(matrix_compteur), config=tessdata_dir_config))

compteur = np.array(Image.open("electricity.jpg").convert('L'))
matrix_compteur_edge = edge_operator(compteur, 5)


