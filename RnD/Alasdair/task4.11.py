import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

c=io.imread("C://Users//kamel//Music//misc//cameraman.tif")

ch=ex.equalize_hist(c)
plt.grid("on")
plt.title("Before equalization")
plt.plot(c,ch,".")
io.imshow(c)
io.show()

plt.grid("on")
plt.title("After equalization")
plt.plot(c,ch,".")
io.imshow(ch)
io.show()
f=plt.figure()
f.show(plt.hist(ch.flatten(),bins=256))
