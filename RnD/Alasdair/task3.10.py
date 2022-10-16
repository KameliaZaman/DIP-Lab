import skimage.io as io
import numpy as np

b = io.imread("C://Users//kamel//Music//misc//4.1.05.tiff")
d=np.reshape(np.random.permutation(16)*16,[4,4])
x=gray2ind(d)

io.imshow(b>np.tile(d,[64,64]))
io.show()
