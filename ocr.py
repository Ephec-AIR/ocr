from PIL import Image
import os
import cv2
import numpy as np
import pytesseract
import time


imgB=cv2.imread('C:/Users/Kevin/Desktop/img05.png')
grayscaled = cv2.cvtColor(imgB,cv2.COLOR_BGR2GRAY)

#filtering image
th = cv2.adaptiveThreshold(grayscaled, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)
th2 = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,1)


th=cv2.bitwise_not(th);
th2=cv2.bitwise_not(th2);
th3=cv2.bitwise_not(th3);

#showing filtered images
cv2.imshow('original',imgB)
cv2.imshow('th.jpg',th)
cv2.imshow('th2.jpg',th2)
cv2.imshow('th3.jpg',th3)

#save temporarely filtered image on disk
cv2.imwrite('th.jpg',th)
cv2.imwrite('th2.jpg',th2)
cv2.imwrite('th3.jpg',th3)

#apply ocr function on each image
for imgpath in ["C:/Users/Kevin/Desktop/img05.png","th.jpg", "th2.jpg", "th3.jpg"]:
    imgfile = Image.open(imgpath)
    imgtext = pytesseract.image_to_string(imgfile,config='-psm 8 --user-patterns C:\Program Files (x86)\Tesseract-OCR\tessdata\eng.user-patterns --user-words C:\Program Files (x86)\Tesseract-OCR\tessdata\eng.user-words bazaar')
    print(imgpath)
    print(imgtext)


#remove filtered images from the disk
for imgpath in ["th.jpg", "th2.jpg", "th3.jpg"]:
    os.remove(imgpath)

cv2.waitKey(0)
cv2.destroyAllWindows()


>>>>>>> af26ea89611496438b4f016481e1b8425f665402
