# -*-coding:Utf-8 -*

import PIL
import os
import numpy as np
import pytesseract as pytes
from PIL import Image
from PIL import ImageFilter
from PIL import ImageColor

img = Image.open("D:\\noela\\Desktop\\mini-compteur.png")
img1 = img.filter(ImageFilter.UnsharpMask(3, 550, 9))

img1 = img1.convert('RGBA')
img1.show()
data = np.array(img1)
red, green, blue, alpha = data.T
white_areas = (red>230) & (blue>230) & (green>230)
rest_areas = (red<=230) & (blue<=230) & (green<=230)

data[..., :-1][white_areas.T] = (0,0,0)
data[..., :-1][rest_areas.T] = (255,255,255)
img2 = Image.fromarray(data)
img2.show()
print("1")
input()
pytes.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
print("2")
input()
retour = pytes.image_to_string(img2)
print("3")
input()
print(retour)

input()
