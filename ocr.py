from platform import system
from re import compile as re_compile
import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageColor, ImageFilter
from imutils import contours, is_cv2
from imutils.perspective import four_point_transform

if system() == "Windows":
    # Patch for windows as tesseract doesnt add itself to the path
    from functools import partial
    pytesseract.image_to_string = partial(pytesseract.image_to_string, 
        config='digits --tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"')
    pytesseract.pytesseract.tesseract_cmd = \
        "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

non_digit_re = re_compile("\D")

class NoThermostaFoundError(Exception):
    pass

def get_consumption(image_path, threshold=150):
    """
    Based on a the path of a image with a digital thermosta somewhere in it,
    returns the interger value showed by the thermosta.

    image_path: ref to ocr.clean_image
    threshold: ref to ocr.binarize_array
    """

    cleaned_image = clean_image(image_path, threshold)
    try:
        thermo = thermosta_crop(cleaned_image)
    except NoThermostaFoundError:
        raise NoThermostaFoundError("No thermosta found for image %s" % image_path)
    Image.fromarray(thermo).save("img.png")
    thermo_value = pytesseract.image_to_string(Image.fromarray(thermo))
    return thermo_value


def thermosta_crop(image):
    """Crop the image rectangulary around "what seems to be a theromosta"."""

    # edge detection
    edges = cv2.Canny(image, 100, 200)

    # find contours in the edge map
    contours = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0 if is_cv2() else 1]
 
    # loop over the size of the contours in descending order
    for contour in sorted(contours, key=cv2.contourArea, reverse=True):
	    # approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
 
        # if the contour has four vertices, then we have found the meter display
        if len(approx) == 4:
            # extract the thermostat display, apply a perspective transform to it
            return four_point_transform(image, approx.reshape(4, 2))
    else:
        # none meter found, raise an error
        raise NoThermostaFoundError()


def clean_image(image_path, threshold):
    """
    Open the image then blur it, gray it and binarize it.

    image_path: path of the image
    threshold: ref to ocr.binarize_array
    """

    img = Image.open(image_path)
    img_blur = img.filter(ImageFilter.UnsharpMask(3, 550, 50))
    img_blur_gray = img_blur.convert('L')
    return binarize_array(np.array(img_blur_gray), threshold)


def binarize_array(numpy_array, threshold):
    """Bellow the threshold: value = 0, above: value = 255"""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            numpy_array[i][j] = 0 if numpy_array[i][j] > threshold else 255
    return numpy_array


def main():
    """Quick test function"""
    mat, mat2 = get_meter("numbers/electricity.jpg", 90)
    img = Image.fromarray(mat)
    img.show()
    img2 = Image.fromarray(mat2)
    img2.show()


if __name__ == "__main__":
    main();
