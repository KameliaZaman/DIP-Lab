import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pyrwt

c = io.imread('C://Users//kamel//Music//misc//4.2.07.tiff')

plt.subplot(2,2,1)
plt.imshow(c)

h,g=rwt.daubcqf(2)
cw1=rwt.dwt(c.astype('float'),h,1)[0]
plt.subplot(2,2,2)
plt.imshow(cw1)

cwlog=np.log(1+abs(cw1))
plt.subplot(2,2,3)
plt.imshow(cwlog)

plt.show()
