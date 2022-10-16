import skimage.io as io
import skimage.filters as fl
import matplotlib.pyplot as plt
import skimage.exposure as ex
 
f = io.imread('C:\\Users\\kamel\\Music\\misc\\7.1.05.tiff')

edge_p=fl.prewitt(f)

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(ex.rescale_intensity(f,out_range=(0.0,1.0)),cmap='gray')

plt.subplot(2,2,2)
plt.axis('off')
plt.title('Filtered image with Prewitt operator')
plt.imshow(ex.rescale_intensity(edge_p,out_range=(0.0,1.0)),cmap='gray')

edge_p=fl.sobel(f)

plt.subplot(2,2,3)
plt.axis('off')
plt.title('Image filtered with Sobel operator')
plt.imshow(ex.rescale_intensity(edge_p,out_range=(0.0,1.0)),cmap='gray')

edge_p=fl.roberts(f)

plt.subplot(2,2,4)
plt.axis('off')
plt.title('Image filtered with Roberts operator')
plt.imshow(ex.rescale_intensity(edge_p,out_range=(0.0,1.0)),cmap='gray')

plt.show()
