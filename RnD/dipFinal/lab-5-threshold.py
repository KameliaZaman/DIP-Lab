import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex
import skimage.filters as fl
import cv2

f = io.imread('C://Users//kamel//Music//misc//7.1.05.tiff')

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f,cmap='gray')

plt.subplot(2,2,2)
plt.axis('off')
plt.title('Single thresholded image')
plt.imshow(ex.rescale_intensity(f<103,out_range=(0.0,1.0)),cmap='gray')

plt.subplot(2,2,3)
plt.axis('off')
plt.title('Double thresholded image')
plt.imshow(ex.rescale_intensity((50<f) & (f<103),out_range=(0.0,1.0)),cmap='gray')

thresh3 = cv2.adaptiveThreshold(f,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

plt.subplot(2,2,4)
plt.axis('off')
plt.title('Adaptive thresholded image')
plt.imshow(ex.rescale_intensity(thresh3,out_range=(0.0,1.0)),cmap='gray')
plt.show()
