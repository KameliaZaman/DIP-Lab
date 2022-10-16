import skimage.io as io
import skimage.data as data
import skimage.util.noise as noise
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img01= data.camera()

plt.subplot(2,2,1)
plt.title('Original')
io.imshow(img01,cmap='gray')

img02= noise.random_noise(img01,mode='s&p',amount=0.10)

plt.subplot(2,2,2)
plt.title('Noisy')
io.imshow(img02,cmap='gray')

img03= ndi.uniform_filter(img02,2)
plt.subplot(2,2,3)
plt.title('Average filtered')
io.imshow(img03,cmap='gray')

img03= ndi.median_filter(img02,3)
plt.subplot(2,2,4)
plt.title('Median filtered')
io.imshow(img03,cmap='gray')

plt.show()

plt.subplot(2,2,1)
plt.title('Original')
io.imshow(img01,cmap='gray')

img02= noise.random_noise(img01,mode='s&p',amount=0.20)

plt.subplot(2,2,2)
plt.title('Noisy')
io.imshow(img02,cmap='gray')

img03= ndi.uniform_filter(img02,2)
plt.subplot(2,2,3)
plt.title('Average filtered')
io.imshow(img03,cmap='gray')

img03= ndi.median_filter(img02,3)
plt.subplot(2,2,4)
plt.title('Median filtered')
io.imshow(img03,cmap='gray')

plt.show()
