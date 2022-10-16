import scipy.ndimage as ndi
import numpy as np

x=np.uint8(np.array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]])*10)

a=np.ones((3,3))/9
print(ndi.convolve(x,a,mode='constant'))
