import numpy as np
import skimage as sk

im=np.zeros((10,10))
im[0:2,0:2]=1
im[0:5,5:9]=1
im[2,1:3]=1
im[3:5,0:2]=1
print(sk.measure.label(im,4,0)+1)
print(sk.measure.label(im,8,0)+1)
