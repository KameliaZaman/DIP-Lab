import numpy as np
import skimage.color
import skimage.io as io
import matplotlib.pyplot as plt
from histograms import histograms

img=io.imread("C://Users//kamel//Music//misc//4.1.05.tiff")
io.imshow(img)
io.show()

histograms,bin_edges=np.histogram(img,bins=256)
plt.figure()
plt.title("Histogram")
plt.xlabel("Gray values")
plt.ylabel("Pixels")
plt.plot(bin_edges[0:-1],histograms)
plt.show()
