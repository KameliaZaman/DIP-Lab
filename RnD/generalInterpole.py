import skimage.io as io
import skimage.transform as tr

c=io.imread('C://Users//kamel//Music//misc//cameraman.tif')
head=c[32:96,89:153]
head4c=tr.rescale(head,4,order=3)
io.imshow(head4c)
io.show()
