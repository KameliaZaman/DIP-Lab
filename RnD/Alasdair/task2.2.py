import numpy as np
import matplotlib.pyplot as plt

img1 = plt.imread('C://Users//kamel//Music//misc//4.1.06.tiff')
nrows, ncols, channels = img1.shape
row, col = np.ogrid[:nrows, :ncols]
cnt_row, cnt_col = nrows/2, ncols/2
outer_disk_mask = ((row - cnt_row) ** 2 + (col - cnt_col) ** 2 > (nrows/2) ** 2)
img1.setflags(write=1)
img1[outer_disk_mask]=0
plt.imshow(img1)
plt.axis('off' )
plt.title('Indexed Image')
plt.show()
plt.imsave('C://Users//kamel//Music//output.png', img1)

