from os import remove
from PIL import Image
import cv2
import pytesseract

def get_consumption(original_image_path):
    filtered_image_path = 'filteredImage.jpg'

    original_image = cv2.imread(original_image_path)
    grayscaled = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    #filtering image
    filtered_image = cv2.adaptiveThreshold(grayscaled, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)
    filtered_image = cv2.bitwise_not(filtered_image)

    #save temporarely filtered image on disk
    cv2.imwrite(filtered_image_path, filtered_image)

    #apply ocr function on filtered image
    imgfile = Image.open(filtered_image_path)
    imgtext = pytesseract.image_to_string(imgfile, config='-psm 6 digits')    

    #remove filtered image from the disk
    remove(filtered_image_path)

    return int(imgtext.replace(" ", ""))
