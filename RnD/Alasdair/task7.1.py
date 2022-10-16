import numpy as np
from numpy.fft import *
a1=np.array([2,3,4,5])

ans1=fft(a1)
print(ans1)

a2=np.array([2,-3,4,-5])

ans2=fft(a2)
print(ans2)

a3=np.array([-9,-8,-7,-6])

ans3=fft(a3)
print(ans3)

a4=np.array([-9,8,-7,6])

ans4=fft(a4)
print(ans4)
