import scipy.ndimage as ndi
import numpy as np
import skimage.io as io
w=io.imread("C://Users//kamel//Music//misc//cameraman.tif")
img=ndi.uniform_filter(w,10)

io.imshow(img)
io.show()
