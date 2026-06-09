"""
Convert to 3 rows × 4 columns
Convert to 2 rows × 6 columns
Print the shape of both arrays using .shape
"""
import numpy as np

data = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr=data.reshape(3,4)
arr1=data.reshape(2,6)
print(arr.shape)
print(arr1.shape)