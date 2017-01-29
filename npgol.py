import numpy as np
# import matplotlib.pyplot as plt

# Z = np.array([[0,0,0,0,0,0],
#               [0,0,0,1,0,0],
#               [0,1,0,1,0,0],
#               [0,0,1,1,0,0],
#               [0,0,0,0,0,0],
#               [0,0,0,0,0,0]])

def inspect_array(array):
  print array + '.dtype : ', array.dtype
  print array + '.shape : ', array.shape

def iterate(Z):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2]                + Z[1:-1,2:] +
         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])

    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
    Z[...] = 0
    Z[1:-1,1:-1][birth | survive] = 1
    return Z

# Z = np.random.randint(0,2,(1080,1920))
# for i in range(100): iterate(Z)
# size = np.array(Z.shape)
# dpi = 72.0
# figsize= size[1]/float(dpi),size[0]/float(dpi)
# fig = plt.figure(figsize=figsize, dpi=dpi, facecolor="white")
# fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
# plt.imshow(Z,interpolation='nearest', cmap=plt.cm.gray_r)
# plt.xticks([]), plt.yticks([])
# plt.show()
