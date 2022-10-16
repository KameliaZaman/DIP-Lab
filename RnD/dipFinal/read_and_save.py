import numpy as np
import matplotlib.pyplot as plt

img1=plt.imread('C:\\Users\\kamel\\Music\\misc\\4.1.06.tiff')
plt.imshow(img1)
plt.axis('off')
plt.title('Tree')
plt.show()

img2=plt.imread('C:\\Users\\kamel\\Music\\misc\\5.3.01.tiff')
plt.imshow(img2,cmap='gray')
plt.axis('off')
plt.show()

plt.imsave('C:\\Users\\kamel\\Music\\misc\\output.png',img1)
