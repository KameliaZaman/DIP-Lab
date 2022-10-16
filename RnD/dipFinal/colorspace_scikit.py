import skimage.io as io
import skimage.data as data
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.color import convert_colorspace

img=data.astronaut()
plt.subplot(2,2,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(img)

img_hsv=convert_colorspace(img,'RGB','HSV')
plt.subplot(2,2,2)
plt.axis('off')
plt.title('RGB to HSV')
plt.imshow(img_hsv)

img_gray=rgb2gray(img)
plt.subplot(2,2,3)
plt.axis('off')
plt.title('RGB to Grayscale')
plt.imshow(img_gray,cmap='gray')
plt.show()
