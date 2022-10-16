import numpy as np
import skimage.data as data
import matplotlib.pyplot as plt

img=data.camera()

plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(img,cmap='gray')

plt.subplot(1,2,2)
plt.title('Thresholded')
plt.imshow(img<20,cmap='gray')

plt.show()
