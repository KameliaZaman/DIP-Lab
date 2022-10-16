import numpy as np
a1=[2,-3,5,6,-2,-1,3,7]
b1=[-1,5,6,4,-3,-5,1,2]
c1=np.convolve(a1,b1)
print(c1)

a2=[7,6,5,4,-4,-5,-6,-7]
b2=[2,2,-5,-5,6,6,-7,-7]
c2=np.convolve(a2,b2)
print(c2)

a3=[2,4,6,8]
b3=[-1,2,-3,4]
c3=np.convolve(a3,b3)
print(c3)

a4=[4,5,6,7]
b4=[3,1,5,-1]
c4=np.convolve(a4,b4)
print(c4)



