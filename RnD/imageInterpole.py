import skimage.io as io
import skimage.transform as tr
import matplotlib.pyplot as plt

c=io.imread('C://Users//kamel//Music//misc//cameraman.tif')
head=c[32:96,89:153]

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(head,cmap='gray')

head4n=tr.rescale(head,2,order=0)
plt.subplot(2,2,2)
plt.axis('off')
plt.title('Order 0 Image')
plt.imshow(head4n,cmap='gray')

head4n=tr.rescale(head,2,order=1)
plt.subplot(2,2,3)
plt.axis('off')
plt.title('Order 1 Image')
plt.imshow(head4n,cmap='gray')
plt.show()
