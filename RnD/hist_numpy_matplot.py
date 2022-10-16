import numpy as np
import matplotlib.pyplot as plt

img1=plt.imread('C:\\Users\\kamel\\Music\\misc\\4.1.01.tiff')

r=img1[:,:,0]
g=img1[:,:,1]
b=img1[:,:,2]

plt.subplot(2,2,1)
plt.title('Original Image')
plt.imshow(img1)

plt.subplot(2,2,2)
plt.title('Red Histogram')
plt.hist(r.flatten(),bins=256)

plt.subplot(2,2,3)
plt.title('Green Histogram')
plt.hist(g.flatten(),bins=256)

plt.subplot(2,2,4)
plt.title('Blue Histogram')
plt.hist(b.flatten(),bins=256)
plt.show()
