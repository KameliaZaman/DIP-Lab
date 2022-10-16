import skimage.transform as tr
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt

r=range(-256,256)
[x,y]=np.meshgrid(r,r)
z=np.sqrt(x**2+y**2)
t=1-((z>254.5) & (z<256))*1

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(t,cmap='gray')

t2=tr.rescale(t,0.25,order=0)
plt.subplot(2,2,2)
plt.axis('off')
plt.title('Order 0 Image')
plt.imshow(t2,cmap='gray')

t3=tr.rescale(t,0.25,order=3)
plt.subplot(2,2,3)
plt.axis('off')
plt.title('Order 3 Image')
plt.imshow(t3,cmap='gray')

t4=tr.rescale(t,0.25,order=3)>0.9
plt.subplot(2,2,4)
plt.axis('off')
plt.title('Order 3 Image')
plt.imshow(t4,cmap='gray')
plt.show()

