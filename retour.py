from fonctions import *
from PIL import Image
import pytesseract

import numpy as np
import matplotlib.pyplot as plt
import cv2

mat, mat2 = get_meter("numbers/electricity.jpg", 90)

img = Image.fromarray(mat)
img.show()
img2 = Image.fromarray(mat2)
img2.show()
