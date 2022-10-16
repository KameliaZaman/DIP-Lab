from skimage import io

b = io.imread("C://Users//kamel//Music//misc//blocks.png")
b2=(b/64)*64
io.imshow(b)
io.show()
io.imshow(b2)
io.show()
