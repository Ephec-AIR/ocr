from ocr import get_consumption
import sys

original_image_path = sys.argv[1]
print('scan in progress: ')
print(get_consumption(original_image_path))
