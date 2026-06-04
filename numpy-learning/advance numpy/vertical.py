"""
💻 Task 6: The "Stack" (Vertical)
Array 1: [1, 2, 3]
Array 2: [4, 5, 6]
The Goal: Use np.vstack to stack them into a 2x3 grid.
"""
import numpy as np
arr=np.array([1,2,3])
arr1=np.array([4,5,6])
print(np.vstack((arr,arr1)))