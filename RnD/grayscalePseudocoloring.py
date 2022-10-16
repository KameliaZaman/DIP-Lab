import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import matplotlib as mpl

b = io.imread('C://Users//kamel//Music//misc//7.2.01.tiff')

plt.subplot(2,2,1)
plt.imshow(b,cmap='gray')

plt.subplot(2,2,2)
plt.imshow(b,cmap=plt.cm.jet)

x=np.array([[1,1,1],[1,0,0],[1,1,0],[0,1,0],[0,1,1],[0,0,1],[1,0,1],[0,0,0]])
vga=np.vstack((4*x[0,:],np.array([[3,3,3]]),4*x[1:,:],2*x[:7,:]))/4.0
b16=b/16
myvga=mpl.colors.ListedColormap(vga)

plt.subplot(2,2,3)
plt.imshow(b16,cmap=myvga)

b4=b/64
mycolormap=mpl.colors.ListedColormap([[0,0,1],[1,0,1],[0,1,0],[1,0,0]])
plt.subplot(2,2,4)
plt.imshow(b4,cmap=mycolormap)

plt.show()
