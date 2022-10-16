import numpy as np
import skimage.io as io
import scipy.ndimage as ndi
import skimage.color as co
import matplotlib.pyplot as plt

k = io.imread('C://Users//kamel//Music//misc//4.2.07.tiff')

plt.subplot(2,2,1)
plt.imshow(k)

u=np.array([[-1,-4,-1],[-4,26,-4],[-1,-4,-1]])/6.0
k2=np.zeros_like(k)

for i in range(3):
    k2[:,:,i]=ndi.convolve(k[:,:,i],u)

plt.subplot(2,2,2)
plt.imshow(k2)

kh=co.rgb2hsv(k)
kh[:,:,2]=ndi.convolve(kh[:,:,2],u)

k3=co.hsv2rgb(kh)

plt.subplot(2,2,3)
plt.imshow(k3)
plt.show()
