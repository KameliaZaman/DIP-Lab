import scipy.ndimage as ndi
import numpy as np
x=np.uint8(np.array([[20,20,20,10,10,10,10,10,10],[20,20,20,20,20,20,20,20,10],[20,20,20,10,10,10,10,20,10],[20,20,10,10,10,10,10,20,10],[20,10,10,10,10,10,10,20,10],[10,10,10,10,20,10,10,20,10],[10,10,10,10,10,10,10,10,10],[20,10,20,20,10,10,10,20,20],[20,10,10,20,10,10,20,10,20]]))
a=np.uint8(np.array([[0,-1,0],[-1,4,-1],[0,-1,0]]))
ndi.correlate(x,a,mode='constant')
