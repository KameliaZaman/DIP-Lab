import skimage.io as io
import matplotlib.pyplot as plt

img1=io.imread('C://Users//kamel//Music//misc//7.2.01.tiff')

plt.subplot(2,2,1)
plt.title("Grayscale Image")
plt.imshow(img1,cmap='gray')

img2=io.imread('C://Users//kamel//Music//misc//4.2.07.tiff')

plt.subplot(2,2,2)
plt.title("RGB Image")
plt.imshow(img2)

img3=io.imread('C://Users//kamel//Music//misc//4.1.06.tiff')

plt.subplot(2,2,3)
plt.title("Indexed Image")
plt.imshow(img3)
plt.show()
