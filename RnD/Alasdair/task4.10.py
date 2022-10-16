import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

img=io.imread("C://Users//kamel//Music//misc//cameraman.tif")
io.imshow(img)
io.show()

ch=ex.equalize_hist(img)
io.imshow(ch)
io.show()

f=plt.figure()
f.show(plt.hist(ch.flatten(),bins=256))
