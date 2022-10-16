import numpy as np
x=10*np.uint8(np.array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]))
print(x)

print(x[0:3,0:3].mean())
print(x[0:3,1:4].mean())
