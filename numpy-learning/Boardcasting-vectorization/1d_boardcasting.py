"""
Task 44: Basic Broadcasting (1D into 2D)
Question: Create a 3×3 matrix of all ones. Create a 1D array [10, 20, 30]. Add them together and print the result.
"""
import numpy as np
matrix = np.ones((3, 3))
array_1d = np.array([10, 20, 30])
result = matrix + array_1d
print(result)