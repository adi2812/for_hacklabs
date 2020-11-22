import numpy as np
import sys 
#method 1 using numpy
def numpy_transpose(matrix):
    return np.transpose(matrix)

#working of numpy_transpose
matrix  =  [[1,2,4],[4,6,5]]

zoom = numpy_transpose(matrix)
sys.stdout.write(str(zoom)) #note
"""note:this was a little unnecessary 
i could have used print function 
instead but i learned this today so wanted to implement"""

#method 2 without any standard library
matrix_1  =  [[1,2,4],[4,6,5]] #for this method we need a resulting matrix too so a 2*3 matrix will have 3*2 matrix as transpose
resulting = [[0,0],[0,0],[0,0]]
def transpose_normal(m,r):
    for i in range(len(m)):
        for j in range(len(m[0])):
            r[j][i] = m[i][j]
    return r
zoom = transpose_normal(matrix_1,resulting)
print(zoom)

