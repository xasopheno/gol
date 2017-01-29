def show(Z):
    for i in range(len(Z[0])):
        print Z[i]
    print '------'

Z = [[0,0,0,0,0,0],
     [0,0,0,1,0,0],
     [0,1,0,1,0,0],
     [0,0,1,1,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]]

show(Z)

def compute_neigbours(array):
    "returns the number of neighbors for each cell and saves it in an array"
    # shape of array
    shape = len(array), len(array[0])
    #makes new array in the same shape
    N  = [[0,]*(shape[0])  for i in range(shape[1])]
    # leaves a border of 0's around the array 
    for x in range(1,shape[0]-1):
        for y in range(1,shape[1]-1):
            N[x][y] = array[x-1][y-1]+array[x][y-1]+array[x+1][y-1] \
                    + array[x-1][y]            +array[x+1][y]   \
                    + array[x-1][y+1]+array[x][y+1]+array[x+1][y+1]
    return N 

def iterate(Z):
    N = compute_neigbours(Z)
    # With a border of zeros...
    shape = len(Z), len(Z[0])
    for x in range(1,shape[0]-1):
        for y in range(1,shape[1]-1):
             if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                 Z[x][y] = 0
             elif Z[x][y] == 0 and N[x][y] == 3:
                 Z[x][y] = 1
    
    return Z

for i in range(4):
    iterate(Z) 
    show(Z)
