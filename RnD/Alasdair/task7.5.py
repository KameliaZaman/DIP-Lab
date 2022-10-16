import numpy as np
from numpy.fft import *
a=np.array([[4,5,-9,-5],[3,-7,1,2],[6,-1,-6,1],[3,-1,7,-5]])

ans=fft(a)
print(ans)

x=fft2(a)
print(x)

