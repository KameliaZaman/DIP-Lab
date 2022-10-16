import scipy.ndimage as ndi
import numpy as np
import skimage.io as io
w=io.imread("C://Users//kamel//Music//misc//cameraman.tif")
a=np.uint8(np.array([[0,-1,0],[-1,4,-1],[0,-1,0]]))
img=ndi.convolve(w,a)

io.imshow(img)
io.show()


