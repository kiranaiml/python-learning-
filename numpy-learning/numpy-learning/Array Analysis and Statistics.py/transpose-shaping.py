"""
Original array
Transposed array
Shape of original array
Shape of transposed array
"""
import numpy as np

data = np.array([
    [1,2,3],
    [4,5,6]
])
print(data)
print(np.transpose(data))
print(np.shape(data))
print(np.shape(np.transpose(data)))