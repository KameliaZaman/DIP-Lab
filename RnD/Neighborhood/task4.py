import scipy.ndimage as ndi
import numpy as np
import skimage.io as io

c=io.imread('C:\\Users\\kamel\\Music\\misc\\cameraman.tif')

f=np.array([[1,4,1],[4,-2,4],[1,4,1]])
cf=ndi.convolve(c,f)
io.imshow(cf)
io.show()

cf2=ndi.convolve(np.float32(c),f,mode='constant')
maxcf2=cf2.max()
mincf2=cf.min()
cf2f=(cf2-mincf2)/(maxcf2-mincf2)
io.imshow(cf2f)
io.show()

io.imshow(cf2/0,vmax=1.0,vmin=0.0)
io.show()
