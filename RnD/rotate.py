import skimage.io as io
import skimage.transform as tr
import matplotlib.pyplot as plt

c=io.imread('C://Users//kamel//Music//misc//cameraman.tif')

cr=tr.rotate(c,60,order=0)
plt.subplot(1,2,1)
plt.axis('off')
plt.imshow(cr,cmap='gray')

crc=tr.rotate(c,60,order=3)
plt.subplot(1,2,2)
plt.axis('off')
plt.imshow(crc,cmap='gray')
plt.show()

