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

x=np.zeros((5,5))
x[2,2]=1

f=ndi.gaussian_filter(x,1,truncate=2)

img02= ndi.convolve(img01,f)

plt.subplot(1,2,2)
plt.axis('off')
plt.title('Gaussian Convolved Image')
plt.imshow(img02,cmap='gray')
plt.show()
