import numpy as np
import skimage.io as io
import skimage.data as data
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img01= data.camera()

plt.subplot(1,2,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(img01,cmap='gray')

img02= ndi.gaussian_filter(img01,5,truncate=3)

plt.subplot(1,2,2)
plt.axis('off')
plt.title('Gaussian Filtered Image')
plt.imshow(img02,cmap='gray')
plt.show()
