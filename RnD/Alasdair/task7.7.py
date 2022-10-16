import skimage.io as io
import numpy as np
import scipy.ndimage as ndi

c = io.imread("C://Users//kamel//Music//misc//cameraman.tif")

cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

io.imshow(cfsl)
io.show()

img=ndi.uniform_filter(c,5)
io.imshow(img)
io.show()
