import numpy as np
import matplotlib.pyplot as plt

img1=plt.imread('C:\\Users\\kamel\\Music\\misc\\4.1.06.tiff')
img2=plt.imread('C:\\Users\\kamel\\Music\\misc\\4.1.04.tiff')

img3=np.bitwise_and(img1,img2)
img4=np.bitwise_or(img1,img2)
img5=np.bitwise_xor(img1,img2)

output=[img1,img2,img3,img4,img5]
titles=['img1','img2','img1 AND img2','img1 OR img2','img1 XOR img2']

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.axis('off')
    plt.title(titles[i])
    plt.imshow(output[i])
plt.show()
