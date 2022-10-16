import skimage.io as io
import numpy as np

img = io.imread("C://Users//kamel//Music//misc//4.1.05.tiff")
D=np.array([[50,100],[150,200]])

img=img.astype(float)
q=img/85
x=q+(q-85*q)
io.imshow(x)
io.show()
