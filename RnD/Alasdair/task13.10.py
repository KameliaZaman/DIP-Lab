import skimage.io as io
import skimage.util.noise as noise
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from scipy.signal import wiener

img01= io.imread('C://Users//kamel//Music//misc//4.2.07.tiff')

plt.subplot(2,2,1)
plt.title('Original')
io.imshow(img01)

img02= noise.random_noise(img01,'gaussian',mean=0,var=0.01)

plt.subplot(2,2,2)
plt.title('Noisy')
io.imshow(img02)

img03= ndi.uniform_filter(img02,2)
plt.subplot(2,2,3)
plt.title('Average filtered')
io.imshow(img03)

img03= wiener(img02,[3,3,3])
plt.subplot(2,2,4)
plt.title('Wiener filtered')
io.imshow(img03)

plt.show()
