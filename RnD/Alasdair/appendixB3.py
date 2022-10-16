import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,2*np.pi,0.1)
plt.plot(x,np.sin(x),x,np.cos(x),'or')
plt.show()

A=np.random.randint(-100,100,size=(10,10))
maxA=abs(A).max()
print(maxA)

B=np.copy(A)
B[np.where(abs(A)==maxA)]=0

C=np.copy(B)
maxB=abs(B).max()
print(maxB)

C[np.where(abs(B)==maxB)]=0

print(abs(C-A))
