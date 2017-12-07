import PIL
import pygame
import cv2
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import matplotlib.pyplot as plt
import scipy.misc

from PIL import Image
from PIL import ImageFilter
from PIL import ImageColor
from scipy import ndimage as ndi
from skimage import feature

def clean_image(image):
    #seuil = 50

    img = Image.open(image)
    img_unsharp = img.filter(ImageFilter.UnsharpMask(3, 550, 9))

    img_unsharp = img_unsharp.convert('L')
    data = np.array(img_unsharp)
    
    #red, green, blue, alpha = data.T
    #white_areas = (red>seuil) & (blue>seuil) & (green>seuil)
    #rest_areas = (red<=seuil) & (blue<=seuil) & (green<=seuil)

    #data[..., :-1][white_areas.T] = (0,0,0)
    #data[..., :-1][rest_areas.T] = (255,255,255)

    #lig, col, balek = data.shape

    #img_gray = np.zeros((lig, col))

    #for i in range(lig-1):
     #   for j in range(col-1):
      #      img_gray[i-1, j-1] = average(data[i-1, j-1])

    data = binarize_array(data, 230)
    
    return data

def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            numpy_array[i][j] = 0 if numpy_array[i][j] > threshold else 255
    return numpy_array

def match_template(img, template):

    w, h, l = template.shape[::-1]
    
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

    return res, min_loc

def correl(matrix, treshold):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = 0 if matrix[i][j] > treshold else 255
    return matrix


def edge_operator(img, sigma):
    edge = feature.canny(img, sigma)
    scipy.misc.imsave('edge.jpg', edge)

    template = np.ones((60, 270))
    template.fill(0)
    for i in range(len(template)):
        template[i][0] = 255
        template[i][269] = 255
    for j in range(len(template[0])):
        template[0][j] = 255
        template[59][j] = 255
    scipy.misc.imsave('template.jpg', template)

    result = match_template(cv2.imread('edge.jpg',1), cv2.imread('template.png',1))

    return result












    


