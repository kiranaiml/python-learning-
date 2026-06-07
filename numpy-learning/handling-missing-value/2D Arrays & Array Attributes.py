"""
Solve these:
Print the value 60
Print the first row
Print the last row
Print the second column
Print the shape of the array
Print the number of dimensions
Print the total number of elements
Print the data type
Expected Concepts
shape
ndim
size
dtype
Row indexing
Column indexing
Element indexing
"""
import numpy as np

data = np.array([
    [12, 24, 36],
    [48, 60, 72],
    [84, 96, 108]
])
print(data[1,1])
print(data[1])
print(data[2])
print(data[:,1])
print(np.shape(data))
print((data.ndim))
print(data.size)