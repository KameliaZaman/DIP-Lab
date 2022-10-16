import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

def bdy4(x):
    return ((x[4]==1) and (x[1]*x[3]*x[5]*x[7]==0))*1
def bdy8(x):
    return (x[4]==1) and (x.prod()==0)

c = io.imread('C://Users//kamel//Music//misc//blob.png')

plt.subplot(2,2,1)
plt.imshow(c,cmap='gray')

c=c.astype('bool')*1
cw=ndi.generic_filter(c,bdy4,size=(3,3))

plt.subplot(2,2,2)
plt.imshow(cw,cmap='gray')

cw8=ndi.generic_filter(c,bdy8,size=(3,3))

plt.subplot(2,2,3)
plt.imshow(cw8,cmap='gray')
plt.show()

