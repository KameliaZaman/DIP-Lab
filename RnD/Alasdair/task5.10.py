import scipy.ndimage as ndi
import numpy as np
import skimage.io as io
import cv2
w=io.imread("C://Users//kamel//Music//misc//cameraman.tif")
img=cv2.Laplacian(w, cv2.CV_16S, ksize=3)

io.imshow(img)
io.show()
