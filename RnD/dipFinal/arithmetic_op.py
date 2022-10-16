import numpy as np
import matplotlib.pyplot as plt

img1=plt.imread('C:\\Users\\kamel\\Music\\misc\\4.1.06.tiff')
img2=plt.imread('C:\\Users\\kamel\\Music\\misc\\4.1.04.tiff')

img3=img1+img2
img4=img1-img2
img5=img2-img1
img6=np.flip(img1,0)
img7=np.flip(img1,1)
img8=np.roll(img1,2048)
img9=np.fliplr(img1)
img10=np.flipud(img1)
img11=np.rot90(img1)

output=[img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11]
titles=['img1','img2','img1+img2','img1-img2','img2-img1','FlipOnce','FlipTwice','Roll','FlipLeft-Right','FlipUp-Down','Rotate90']

for i in range(11):
    plt.subplot(3,4,i+1)
    plt.axis('off')
    plt.title(titles[i])
    plt.imshow(output[i])
plt.show()
