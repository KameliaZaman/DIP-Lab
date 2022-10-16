import scipy.ndimage as ndi
import numpy as np
import skimage.io as io

c=io.imread('C:\\Users\\kamel\\Music\\misc\\cameraman.tif')
u=np.array([[-2,-2,-2],[-2,25,-2],[-2,-2,-2]])/9.0
ku=ndi.convolve(c.astype(float),u)
io.imshow(ku/255,vmax=1.0,vmin=0.0)
io.show()
