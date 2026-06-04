#Create a 3x3 array of integers. Use the .itemsize property to find out how many bytes each single number in that array is using.
import numpy as np
arr_3d=np.array([[1,2,3],[4,5,6]])
print(arr_3d.itemsize)