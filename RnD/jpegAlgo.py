import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
from scipy.fftpack import dct

def dct2(x):
    return dct(dct(x,norm='ortho').T,norm='ortho').T

def jpg_in(x,n):
    bd=dct2(np.float64(x)-128)
    return np.round(bd/(q*n))
c = io.imread('C://Users//kamel//Music//misc//7.2.01.tiff')

plt.subplot(2,2,1)
plt.imshow(c)

x,y=150,90
block=c[x:x+8,y:y+8]
b=block.astype('float64')-128

c=c.astype('float64')
rs,cs=c.shape
cjl=np.zeros_like(c)
for i in range(0,rs,8):
    for j in range(0,cs,8):
        cjl[i:i+8,j:j+8]=jpg_in(c[i:i+8,j:j+8],1)

print(len(np.where(abs(cjl)<1)[0]))

plt.subplot(2,2,2)
plt.imshow(cjl)
plt.show()
