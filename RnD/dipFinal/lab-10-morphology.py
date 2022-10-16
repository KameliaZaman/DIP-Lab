import numpy as np
from skimage.morphology import binary_dilation as bwdilate, binary_erosion as bwerode, binary_opening as bwopen, binary_closing as bwclose, skeletonize as bwskel
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt

c = plt.imread('C:\\Users\\kamel\\Music\\misc\\blob.png')
sel = np.ones((3,3))
c_01 = bwdilate(c,sel)


plt.subplot(2,3,1)
plt.axis('off')
plt.title('Binary image')
plt.imshow(c, cmap='gray')

plt.subplot(2,3,2)
plt.axis('off')
plt.title('Dilation of the binary image')
plt.imshow(ex.rescale_intensity(c_01,out_range=(0.0,1.0)),cmap='gray')

c_01 = bwerode(c,sel)

plt.subplot(2,3,3)
plt.axis('off')
plt.title('Erosion of the binary image')
plt.imshow(ex.rescale_intensity(c_01,out_range=(0.0,1.0)),cmap='gray')

c_01 = bwopen(c,sel)

plt.subplot(2,3,4)
plt.axis('off')
plt.title('Opening of the binary image')
plt.imshow(ex.rescale_intensity(c_01,out_range=(0.0,1.0)),cmap='gray')

c_01 = bwclose(c,sel)

plt.subplot(2,3,5)
plt.axis('off')
plt.title('Closing of the binary image')
plt.imshow(ex.rescale_intensity(c_01,out_range=(0.0,1.0)),cmap='gray')

c_01 = bwskel(c)

plt.subplot(2,3,6)
plt.axis('off')
plt.title('Skeletonization of the binary image')
plt.imshow(ex.rescale_intensity(c_01,out_range=(0.0,1.0)),cmap='gray')

plt.show()
