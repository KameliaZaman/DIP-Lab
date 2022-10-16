import numpy as np
import matplotlib.pyplot as plt

img1=plt.imread('C:\\Users\\kamel\\Music\\misc\\4.1.06.tiff')
print('image1 type: ',type(img1))
print('image1 shape: ',img1.shape)
print('image1 no. of dimension: ',img1.ndim)
print('image1 size: ',img1.size)
print('image1 data type: ',img1.dtype)
print('image1 no. of bytes: ',img1.nbytes)

img2=plt.imread('C:\\Users\\kamel\\Music\\misc\\5.3.01.tiff')
print('image2 type: ',type(img2))
print('image2 shape: ',img2.shape)
print('image2 no. of dimension: ',img2.ndim)
print('image2 size: ',img2.size)
print('image2 data type: ',img2.dtype)
print('image2 no. of bytes: ',img2.nbytes)

print('img1[10,10,0]: ',img1[10,10,0])
print('img1[10,10,1]: ',img1[10,10,1])
print('img1[10,10,2]: ',img1[10,10,2])

print('img1[10,10,:]: ',img1[10,10,:])
print('img2[10,10]: ',img2[10,10])
