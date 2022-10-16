from skimage import color
from skimage import io

img = io.imread("C://Users//kamel//Music//misc//emu.png")[:,:,:3]
imgGray = color.rgb2gray(img)

print(imgGray.dtype)
io.imshow(imgGray)
io.show()
