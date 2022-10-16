import PIL
from PIL import Image
import skimage.io as io
import cv2

image = io.imread("C://Users//kamel//Music//misc//5.3.01.tiff")
if(len(image.shape)<3):
      print('Grayscale')
elif len(image.shape)==3:
      print('Color(RGB)')
else:
      print('Binary')
io.imshow(image)
cv2.imshow('Grayscale image of a man', image)

image1 = PIL.Image.open('C://Users//kamel//Music//misc//5.3.01.tiff')
width, height = image1.size

print(width, height)
