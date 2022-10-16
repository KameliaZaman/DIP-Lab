import numpy as np
x,y=np.mgrid[0:256,0:256].astype(float)
z=np.sqrt((x-128)**2+(y-128)**2)
z2=z.max()-z
print(z2)
