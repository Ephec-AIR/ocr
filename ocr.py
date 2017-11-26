from PIL import Image
import os
import cv2
import pytesseract

def get_consumption(originalImagePath):
    filteredImagePath='filteredImage.jpg'
    
    originalImage = cv2.imread(originalImagePath)
    grayscaled = cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)

    #filtering image
    filteredImage = cv2.adaptiveThreshold(grayscaled, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)
    filteredImage = cv2.bitwise_not(filteredImage);
     
    #save temporarely filtered image on disk
    cv2.imwrite(filteredImagePath,filteredImage)
    
    #apply ocr function on filtered image
    imgfile = Image.open(filteredImagePath)
    imgtext = pytesseract.image_to_string(imgfile,config='-psm 6 digits')    
    
    #remove filtered image from the disk
    os.remove(filteredImagePath)
    
    return int(imgtext.replace(" ", ""))


