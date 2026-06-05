"""
Task 53: Vectorized Thresholding (Clipping Data)
Question: Create an array with the values [15, 62, 78, 34, 99, 12, 45, 85, 23, 50]. Use vectorization and conditional masking to replace all values greater than 50 with the number 100. Print the modified array.
"""
import numpy as np
a=np.array([2,4,54,56,7,7,8,87,6,54,43,23])
a[a>50]=100
print(a)