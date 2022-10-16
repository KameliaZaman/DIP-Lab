import PIL
from PIL import Image
import skimage.io as io
import cv2

image = io.imread("C://Users//kamel//Music//misc//5.2.10.tiff")
io.imshow(image)
cv2.imwrite('C://Users//kamel//Music//misc//New1.jpeg',image)
cv2.imwrite('C://Users//kamel//Music//misc//New2.png',image)
cv2.imwrite('C://Users//kamel//Music//misc//New3.bmp',image)

image1 = PIL.Image.open('C://Users//kamel//Music//misc//New1.jpeg')
width, height = image1.size

print("jpeg size: ",width, height)

image2 = PIL.Image.open('C://Users//kamel//Music//misc//New2.png')
width1, height1 = image2.size

print("png size: ",width1, height1)

image3 = PIL.Image.open('C://Users//kamel//Music//misc//New3.bmp')
width2, height2 = image3.size

print("bmp size: ",width2, height2)
