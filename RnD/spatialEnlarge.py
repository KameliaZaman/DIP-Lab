import skimage.io as io
import scipy.ndimage as ndi
import numpy as np
import matplotlib.pyplot as plt

c=io.imread('C://Users//kamel//Music//misc//cameraman.tif')
head=c[32:96,89:153]
r,c=head.shape
hz=np.zeros((2*r,2*c)).astype('uint8')
hz[::2,::2]=head
ne=np.array([[0,0,0],[0,1,1],[0,1,1]])
bi=np.array([[1,2,1],[2,4,2],[1,2,1]])/4.0
bc=np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])/64.0

plt.subplot(2,2,1)
plt.axis('off')
plt.imshow(ndi.correlate(hz,ne),cmap='gray')

plt.subplot(2,2,2)
plt.axis('off')
plt.imshow(ndi.correlate(hz,bi),cmap='gray')

plt.subplot(2,2,3)
plt.axis('off')
plt.imshow(ndi.correlate(hz,bc),cmap='gray')
plt.show()
