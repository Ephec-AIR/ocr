from PIL import Image
import os
import cv2
import numpy as np
import pytesseract
import time


imgB=cv2.imread('img02.jpg')
grayscaled = cv2.cvtColor(imgB,cv2.COLOR_BGR2GRAY)

#filtering image
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval2,th3 = cv2.threshold(grayscaled,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th2 = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

#showing filtered images
cv2.imshow('original',imgB)
cv2.imshow('Adaptative trh.',th)
cv2.imshow('Adaptative trh. other param',th2)
cv2.imshow('OTSU threshold',th3)

#save temporarely filtered image on disk
cv2.imwrite('th.jpg',th)
cv2.imwrite('th2.jpg',th2)
cv2.imwrite('th3.jpg',th3)

for imgpath in ["th.jpg", "th2.jpg", "th3.jpg"]:
    imgfile = Image.open(imgpath)
    imgtext = pytesseract.image_to_string(imgfile)
    print(imgtext)

#apply OCR on filt

time.sleep(5)
#remove filtered images from the disk
#os.remove('th.jpg')
#os.remove('th2.jpg')
#os.remove('th3.jpg')

cv2.waitKey(0)
cv2.destroyAllWindows()


