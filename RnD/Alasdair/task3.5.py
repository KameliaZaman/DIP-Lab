from PIL import Image
from skimage import io

image_path = "C://Users//kamel//Music//misc//buffalo.png"
image_file1 = Image.open(image_path)

image_file = image_file1.convert('RGB')

image_file.save("C://Users//kamel//Music//misc//buffalo1.jpg", quality=25)

image_file.save("C://Users//kamel//Music//misc//buffalo2.jpg", quality=1)

img = io.imread("C://Users//kamel//Music//misc//buffalo1.jpg")
img2 = io.imread("C://Users//kamel//Music//misc//buffalo2.jpg")
io.imshow(img)
io.show()
io.imshow(img2)
io.show()
