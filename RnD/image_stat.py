import numpy as np
import matplotlib.pyplot as plt

img1=plt.imread('C:\\Users\\kamel\\Music\\misc\\4.1.06.tiff')
print('img min pixel: ',img1.min())
print('img max pixel: ',img1.max())
print('img mean: ',img1.mean())
print('img median: ',np.median(img1))
print('img average: ',np.average(img1))
print('img mean: ',np.mean(img1))
print('img standard deviation: ',np.std(img1))
print('img variance: ',np.var(img1))
