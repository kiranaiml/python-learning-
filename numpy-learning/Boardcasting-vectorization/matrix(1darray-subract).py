"""
Task 48: Matrix and 1D Array Subtraction
Question: Create a 3×4 matrix containing any numbers. Create a 1D array of shape (4,) containing any numbers. Subtract this 1D array from the matrix and print the result.
"""
import numpy as np
a=np.ones((2,4))
b=np.array([1,2,3,4])
result=a-b
print(result)