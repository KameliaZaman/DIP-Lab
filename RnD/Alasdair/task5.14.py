import scipy.ndimage as ndi
import numpy as np
import skimage.io as io
import cv2
w=io.imread("C://Users//kamel//Music//misc//cameraman.tif")
img=ndi.median_filter(w, size=20,mode='repeat')
io.imshow(img)
io.show()
