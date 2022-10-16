import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

c = io.imread('C://Users//kamel//Music//misc//7.2.01.tiff')

plt.subplot(2,2,1)
plt.imshow(c)

c=c.astype('bool')*1
c2=np.pad(c,[1,1],mode='constant').astype('float64')
c2[np.where(c2==0)]=float('inf')
c2[np.where(c2==1)]=0
fmask=np.array([[4,3,3],[3,0,0],[0,0,0]])
bmask=np.array([[0,0,0],[0,0,3],[4,3,3]])

for i in range(256):
    for j in range(256):
        c2[i+1,j+1]=(c2[i:i+3,j:j+3]+fmask).min()

for i in range(256)[::-1]:
    for j in range(256)[::-1]:
        c2[i+1,j+1]=(c2[i:i+3,j:j+3]+bmask).min()        

plt.subplot(2,2,2)
plt.imshow(c2[1:257,1:257])

plt.show()

