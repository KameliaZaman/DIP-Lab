import skimage.io as io

img = io.imread("C://Users//kamel//Music//misc//4.1.05.tiff")
img1 = (img/64)
io.imshow(img1)
io.show()
