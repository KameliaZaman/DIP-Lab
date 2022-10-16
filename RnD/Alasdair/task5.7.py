import scipy.ndimage as ndi
import numpy as np
import skimage.io as io
w=io.imread("C://Users//kamel//Music//misc//cameraman.tif")
img=ndi.gaussian_filter(w,[3,3],truncate=0.5)
io.imshow(img)
io.show()

img2=ndi.gaussian_filter(w,[3,3],truncate=1)
io.imshow(img2)
io.show()

img3=ndi.gaussian_filter(w,[3,3],truncate=2)
io.imshow(img3)
io.show()

img4=ndi.gaussian_filter(w,[7,7],truncate=1)
io.imshow(img4)
io.show()

img5=ndi.gaussian_filter(w,[7,7],truncate=3)
io.imshow(img5)
io.show()

img6=ndi.gaussian_filter(w,[7,7],truncate=6)
io.imshow(img6)
io.show()

img7=ndi.gaussian_filter(w,[11,11],truncate=1)
io.imshow(img7)
io.show()

img8=ndi.gaussian_filter(w,[11,11],truncate=4)
io.imshow(img8)
io.show()

img9=ndi.gaussian_filter(w,[11,11],truncate=8)
io.imshow(img9)
io.show()

img10=ndi.gaussian_filter(w,[21,21],truncate=1)
io.imshow(img10)
io.show()

img11=ndi.gaussian_filter(w,[21,21],truncate=5)
io.imshow(img11)
io.show()

img12=ndi.gaussian_filter(w,[21,21],truncate=10)
io.imshow(img12)
io.show()
