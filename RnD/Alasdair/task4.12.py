import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

img=io.imread("C://Users//kamel//Music//misc//7.1.08.tiff")

x=ex.equalize_hist(img)
plt.grid("on")
plt.xlabel("gray value")
plt.ylabel("pixels")
plt.title("Image")
plt.plot(img,x,".")
io.imshow(img)
io.show()

plt.grid("on")
plt.xlabel("gray value")
plt.ylabel("pixels")
plt.title("Image")
plt.plot(img,x,".")
io.imshow(x)
io.show()
