"""
💻 Task 20: Append & Reshape (Mixed)
The Challenge: Start with a 1D array of 3 elements (like [1, 2, 3]).
The Goal: Append one more element (to make it 4 elements total) and then reshape it into a 2x2 array.
The Rule: You must do this in one single line of code inside the print() function.
"""
import numpy as np
arr=np.array([1,2,3])
print(np.append(arr,4).reshape(2,2))