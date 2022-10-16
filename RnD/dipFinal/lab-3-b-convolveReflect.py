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

f=np.ones((9,9))/81

img02= ndi.convolve(img01, f, mode='reflect')

plt.subplot(1,2,2)
plt.axis('off')
plt.title('Reflect Convolved Image')
plt.imshow(img02,cmap='gray')
plt.show()
