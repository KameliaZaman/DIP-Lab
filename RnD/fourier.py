import skimage.io as io
import numpy as np
import scipy.ndimage as ndi

c = io.imread("C://Users//kamel//Music//misc//7.2.01.tiff")

cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

io.imshow(cfsl)
io.show()

c = io.imread("C://Users//kamel//Music//misc//4.2.07.tiff")

cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

io.imshow(cfsl)
io.show()

c = io.imread("C://Users//kamel//Music//misc//4.1.06.tiff")

cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

io.imshow(cfsl)
io.show()
