import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
from skimage.color import rgb2hsv
import colorsys

x = io.imread('C://Users//kamel//Music//misc//4.2.07.tiff')
print(x.shape)

plt.subplot(4,4,1)
plt.imshow(x)
a=1
for i in range(3):
    a=a+1
    plt.subplot(4,4,a)
    plt.imshow(x[:,:,i])

xh=rgb2hsv(x)
for i in range(3):
    a=a+1
    plt.subplot(4,4,a)
    plt.imshow(xh[:,:,i])

xyiq=colorsys.rgb_to_yiq(*np.dsplit(x,3))
for i in range(3):
    a=a+1
    plt.subplot(4,4,a)
    plt.imshow(xyiq[i][:,:,0])

rgb2yiq=np.array([[.299,.587,.114],[.596,-.275,-.321],[.212,-.528,.311]])
xyiq=x.dot(rgb2yiq)
for i in range(3):
    a=a+1
    plt.subplot(4,4,a)
    plt.imshow(xyiq[:,:,i])

plt.show()
