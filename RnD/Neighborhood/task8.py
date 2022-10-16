import scipy.ndimage as ndi
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

c=io.imread('C:\\Users\\kamel\\Music\\misc\\cameraman.tif')
cmax=ndi.generic_filter(c,max,[3,3])
io.imshow(cmax)
io.show()

cmin=ndi.minimum_filter(c,size=(3,3))
io.imshow(cmin)
io.show()

cm=ndi.median_filter(c,size=(3,3))
io.imshow(cm)
io.show()
cm2=ndi.rank_filter(c,4,size=(3,3))
io.imshow(cm2)
io.show()
