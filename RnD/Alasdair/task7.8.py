import skimage.io as io
import numpy as np
import scipy.ndimage as ndi

c = io.imread("C://Users//kamel//Music//misc//cameraman.tif")

io.imshow(c)
io.show()

cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

io.imshow(cfsl)
io.show()

cf2 = np.fft.fft2(cfsl)
cfs2 = np.fft.fftshift(cf2)
cfsl2 = np.log(1+np.abs(cfs2))

io.imshow(cfsl2)
io.show()
