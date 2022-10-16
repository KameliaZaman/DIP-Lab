import skimage.io as io
import numpy as np
from numpy.fft import *
import skimage.exposure as ex

img = io.imread("C://Users//kamel//Music//misc//cameraman.tif")

io.imshow(img)
io.show()

cf = np.fft.fft2(img)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

io.imshow(cfsl)
io.show()

d=15
ar=range(-128,128)
x,y=np.meshgrid(ar,ar)
c=(x**2+y**2<d**2)*1
cfl=cfs*c

io.imshow(abs(ifft2(cfl)))
io.show()

c2=(x**2+y**2>d**2)*1
cfl2=cfs*c2

io.imshow(abs(ifft2(cfl2)))
io.show()

bl=1/(1+((x**2+y**2)/d**2)**2)
cfbl=cfs*bl
io.imshow(ex.rescale_intensity(abs(ifft2(cfbl)),out_range=(0.0,1.0)))
io.show()

bh=1-1/(1+((x**2+y**2)/d**2)**2)
cfbh=cfs*bh

io.imshow(abs(ifft2(cfbh)))
io.show()

sigma=10
g=np.exp(-(x**2+y**2)/sigma**2)
g1=g/g.sum()
cg1=cfs*g1

io.imshow(abs(ifft2(cg1)))
io.show()

h1=1-g/g.max()
ch1=cfs*h1

io.imshow(abs(ifft2(ch1)))
io.show()
