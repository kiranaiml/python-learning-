#Create an array of integers from 1 to 10 and convert it to float64 using astype.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
floatarr_= arr.astype(float)
print("Array :" , floatarr_)
print("Data Type :" , floatarr_.dtype)