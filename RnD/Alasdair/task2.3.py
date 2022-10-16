import skimage.io as io
image = io.imread("C://Users//kamel//Music//misc//4.1.04.tiff")
if(len(image.shape)<3):
      print('Grayscale')
elif len(image.shape)==3:
      print('Color(RGB)')
else:
      print('Binary')
io.imshow(image)
io.show()
