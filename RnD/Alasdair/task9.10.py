import skimage.data as data
import skimage.filters as fl
import matplotlib.pyplot as plt
import numpy as np
from skimage import feature

def zero_cross_detection(image):
    z_c_image = np.zeros(image.shape)

    for i in range(0,image.shape[0]-1):
        for j in range(0,image.shape[1]-1):
            if image[i][j]>0:
                if image[i+1][j] < 0 or image[i+1][j+1] < 0 or image[i][j+1] < 0:
                    z_c_image[i,j] = 1
            elif image[i][j] < 0:
                if image[i+1][j] > 0 or image[i+1][j+1] > 0 or image[i][j+1] > 0:
                    z_c_image[i,j] = 1
    return z_c_image

f = data.camera()

edge_p=fl.roberts(f)

plt.subplot(3,3,1)
plt.title('Original image')
plt.imshow(f,cmap='gray')

plt.subplot(3,3,2)
plt.title('Filtered image with Roberts operator')
plt.imshow(edge_p,cmap='gray')

edge_p=fl.prewitt(f)

plt.subplot(3,3,3)
plt.title('Image filtered with Prewitt operator')
plt.imshow(edge_p,cmap='gray')

edge_p=fl.sobel(f)

plt.subplot(3,3,4)
plt.title('Image filtered with Sobel operator')
plt.imshow(edge_p,cmap='gray')

edge_p=fl.laplace(f)

plt.subplot(3,3,5)
plt.title('Image filtered with Laplacian operator')
plt.imshow(edge_p,cmap='gray')

edge_p=zero_cross_detection(f)

plt.subplot(3,3,6)
plt.title('Image filtered with Zero-crossing operator')
plt.imshow(edge_p,cmap='gray')

edge_p=feature.canny(f)

plt.subplot(3,3,7)
plt.title('Image filtered with Canny operator')
plt.imshow(edge_p,cmap='gray')

plt.show()
