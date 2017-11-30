from os import remove
from PIL import Image
import cv2
import pytesseract
import sys

def test_treshold_params(original_image_path):
    filtered_image_path = 'compteurs_opti/filtredImage'
    resized_image_path = 'compteurs_opti/resizedImage.jpg'

    original_image_big = Image.open(original_image_path)
    original_image_big.thumbnail((200,200), Image.ANTIALIAS)
    original_image_big = original_image_big.crop((20,50,180,100))
    original_image_big.save(resized_image_path)
    
    
    original_image = cv2.imread(resized_image_path)
    
    #removing noise and setting grey scale
    noise_filtering = cv2.fastNlMeansDenoisingColored(original_image,None,10,10,7,21)
    grayscaled = cv2.cvtColor(noise_filtering, cv2.COLOR_BGR2GRAY)

    #filtering image
    i=0
    
    filtered_image = cv2.adaptiveThreshold(grayscaled, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,201,1)
    if sys.argv[3] == 'inv':
        filtered_image = cv2.bitwise_not(filtered_image)
            
           
    cv2.imwrite(filtered_image_path + '.jpg', filtered_image)
    imgfile = Image.open(filtered_image_path + '.jpg')
    #OCR reading
    value_on_image = (pytesseract.image_to_string(imgfile, config='-psm 4 digits')).replace(" ", "")
    print(value_on_image)    
    

    
                
            
        

test_treshold_params(sys.argv[1])
