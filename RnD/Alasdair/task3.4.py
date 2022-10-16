import skimage.util as ut

from skimage import color
from skimage import io

img = io.imread("C://Users//kamel//Music//misc//cameraman.tif")[:,:3]
e = color.rgb2gray(img)

e2=ut.img_as_ubyte(e)

print(e2.dtype)
