import PIL
import pygame
import cv2
import numpy as np
#np.seterr(divide='ignore', invalid='ignore')
import matplotlib.pyplot as plt
import scipy.misc

from PIL import Image
from PIL import ImageFilter
from PIL import ImageColor
from scipy import ndimage as ndi
from skimage import feature

def clean_image(image):
    seuil = 70

    img = Image.open(image)
    img_gray = img.convert('L')

    data = np.array(img_gray)
    data = binarize_array(data, seuil)

    img2 = Image.fromarray(data)
    
    img_unsharp = img2.filter(ImageFilter.UnsharpMask(3, 550, 50))
    img_unsharp = img_unsharp.convert('L')
    
    #red, green, blue = data.T
    #white_areas = (red>seuil) & (blue>seuil) & (green>seuil)
    #rest_areas = (red<=seuil) & (blue<=seuil) & (green<=seuil)

    #data[..., :-1][white_areas.T] = (0,0,0)
    #data[..., :-1][rest_areas.T] = (255,255,255)

    #lig, col, balek = data.shape

    #img_gray = np.zeros((lig, col))

    #for i in range(lig-1):
     #   for j in range(col-1):
      #      img_gray[i-1, j-1] = average(data[i-1, j-1])
    
    return img_unsharp

def binarize_array(numpy_array, threshold):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            numpy_array[i][j] = 255 if numpy_array[i][j] > threshold else 0
    return numpy_array

def match_template(img, template):

    w, h = template.shape[::-1]
    
    # Apply template Matching
    res = cv2.matchTemplate(img, template, 4)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = min_loc
    
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    
    plt.show()

    return res

def correl(matrix, treshold):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = 0 if matrix[i][j] > treshold else 255
    return matrix















    


