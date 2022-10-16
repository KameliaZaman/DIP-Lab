import numpy as np
import skimage.io as io
import skimage.exposure as ex
import matplotlib.pyplot as plt

img01= io.imread('C:\\Users\\kamel\\Music\\misc\\7.2.01.tiff')

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(img01,cmap='gray')

img02= ex.adjust_gamma(img01,0.5)

plt.subplot(2,2,2)
plt.axis('off')
plt.title('Adjusted Image')
plt.imshow(img02,cmap='gray')

plt.subplot(2,2,3)
plt.title('Adjusted Image Histogram')
plt.hist(img02.flatten(), bins=256)

plt.show()
