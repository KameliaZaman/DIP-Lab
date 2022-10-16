import skimage.io as io
import skimage.data as data
import matplotlib.pyplot as plt

img=io.imread('C:\\Users\\kamel\\Music\\misc\\4.2.05.tiff')
print(type(img))

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Plane')
plt.imshow(img)

img=data.astronaut()
plt.subplot(2,2,2)
plt.axis('off')
plt.title('Astronaut')
plt.imshow(img)

img=data.coffee()
plt.subplot(2,2,3)
plt.axis('off')
plt.title('Coffee')
plt.imshow(img)

img=data.binary_blobs(length=512,blob_size_fraction=0.1,seed=5)
plt.subplot(2,2,4)
plt.axis('off')
plt.title('Blobs')
plt.imshow(img,cmap='gray')

plt.show()
