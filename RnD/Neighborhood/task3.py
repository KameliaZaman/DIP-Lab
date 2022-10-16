import scipy.ndimage as ndi
import numpy as np
import skimage.io as io

c=io.imread('C:\\Users\\kamel\\Music\\misc\\cameraman.tif')
cf=ndi.convolve(c,np.ones((9,9))/81,mode='constant')
io.imshow(cf)
io.show()

cf=ndi.uniform_filter(c,[9,9],mode='constant')
io.imshow(cf)
io.show()

cf=ndi.uniform_filter(c,25)
io.imshow(cf)
io.show()

cf=ndi.uniform_filter(c,50)
io.imshow(cf)
io.show()
