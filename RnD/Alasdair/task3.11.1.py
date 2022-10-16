import skimage.io as io
from PIL import Image
import numpy
import scipy

def fs(im,k):
    rs,cs=im.shape
    ed=array([[0,0,7],[3,5,1]])/16.0
    z=zeros((rs+2,cs+2))
    z[1:rs+1,1:cs+1]=float64(im)
    for i in range(1,rs+1):
        for j in range(1,cs+1):
            old=z[i,j]
            new=(old//(255//k))*(255//(k-1))
            z[i,j]=new
            E=old-new
            z[i:i+2,j-1:j+2]=z[i:i+2,j-1:j+2]+E*ed;
    return uint8(z[1:rs+1,1:cs+1])

img = io.imread("C://Users//kamel//Music//misc//4.1.05.tiff")
img2 = Image.fromarray(numpy.uint8(scipy.signal.deconvolve))

img3=fs(img2,2)
io.imshow(img3)
io.show()
