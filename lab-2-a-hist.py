import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

img = io.imread('C:\\Users\\kamel\\Music\\misc\\7.2.01.tiff')

plt.subplot(1,2,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(img,cmap='gray')

plt.subplot(1,2,2)
plt.title('Image Histogram')
plt.hist(img.flatten(), bins=256)

plt.show()
