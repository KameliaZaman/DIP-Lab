import scipy.ndimage as ndi
import numpy as np
import skimage.io as io

c=io.imread('C:\\Users\\kamel\\Music\\misc\\cameraman.tif')

cg1=ndi.gaussian_filter(c,0.5,truncate=4.5)
io.imshow(cg1)
io.show()
cg2=ndi.gaussian_filter(c,2,truncate=1)
io.imshow(cg2)
io.show()
cg3=ndi.gaussian_filter(c,1,truncate=5)
io.imshow(cg3)
io.show()
cg4=ndi.gaussian_filter(c,5,truncate=1)
io.imshow(cg4)
io.show()

x=np.ones((5,5))
x[2,2]=1

print(ndi.gaussian_filter(x,1,truncate=2).round(7))
