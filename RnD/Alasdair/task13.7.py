import numpy as np
import skimage.io as io
import skimage.exposure as ex
import skimage.color as co
import matplotlib.pyplot as plt

s = io.imread('C://Users//kamel//Music//misc//street.jpg')[:,:,:3]

plt.subplot(2,2,1)
plt.imshow(s)

s2=np.zeros_like(s.astype('float64'))
for i in range(3):
    s2[:,:,i]=ex.equalize_hist(s[:,:,i])
plt.subplot(2,2,2)
plt.imshow(s2)

sh=co.rgb2hsv(s)
sh[:,:,2]=ex.equalize_hist(sh[:,:,2])
s2=co.hsv2rgb(sh)
plt.subplot(2,2,3)
plt.imshow(s2)

plt.show()
