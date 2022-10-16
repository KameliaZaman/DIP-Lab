import scipy.ndimage as ndi
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

c=io.imread('C:\\Users\\kamel\\Music\\misc\\cameraman.tif')
kf=ndi.uniform_filter(c,3)
hb1=3*c-2*kf
hb2=1.25*c-0.25*kf
io.imshow(hb1,vmax=1.0,vmin=0.0)
io.show()

io.imshow(hb2,vmax=1.0,vmin=0.0)
io.show()
