import numpy as np
import skimage.io as io
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img01= io.imread('C:\\Users\\kamel\\Music\\misc\\7.2.01.tiff')

plt.subplot(1,2,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(img01,cmap='gray')

f=np.ones((3,3))/9

img02= ndi.convolve(img01, f, mode='constant')

plt.subplot(1,2,2)
plt.axis('off')
plt.title('Constant Convolved Image')
plt.imshow(img02,cmap='gray')
plt.show()
