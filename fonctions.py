import PIL
import cv2
import numpy as np
import pytesseract
import imutils

from PIL import Image
from PIL import ImageFilter
from PIL import ImageColor
from imutils.perspective import four_point_transform
from imutils import contours

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

def get_meter(image, threshold):

    # image cleanup
    meter_clean_matrice = clean_image(image, threshold)
    meter_clean_img = Image.fromarray(meter_clean_matrice)

    # edge detection
    edge = cv2.Canny(meter_clean_matrice, 100, 200)
    invert_edge = invert_array(np.array(edge))
    
    # find contours in the edge map, then sort them by their
    # size in descending order
    cnts = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    displayCnt = None
 
    # loop over the contours
    for c in cnts:
	# approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	# if the contour has four vertices, then we have found
	# the meter display
        if len(approx) == 4:
            displayCnt = approx
            break
    # extract the thermostat display, apply a perspective transform
    # to it
    output = four_point_transform(meter_clean_matrice, displayCnt.reshape(4, 2))
    
    #print(pytesseract.image_to_string(output, config=tessdata_dir_config))
    return output, invert_edge

def clean_image(image, threshold):

    img = Image.open(image)
    img_gray = img.convert('L')

    img_unsharp = img_gray.filter(ImageFilter.UnsharpMask(3, 550, 50))
    img_unsharp = img_unsharp.convert('L')

    data = np.array(img_unsharp)
    data = binarize_array(data, threshold)
    
    return data

def binarize_array(numpy_array, threshold):

    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            numpy_array[i][j] = 0 if numpy_array[i][j] > threshold else 255
    return numpy_array

def invert_array(numpy_array):

    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            numpy_array[i][j] = 255 if numpy_array[i][j] == 0 else 0
    return numpy_array
    




















    
