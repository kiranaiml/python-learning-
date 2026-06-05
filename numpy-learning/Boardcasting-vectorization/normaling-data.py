"""
Task 52: Normalizing Data (Vector L2 Norm)
Let's see if you can use a similar logic for dividing instead of subtracting.
Question: Create a 1D array with the values [3, 4, 12]. Calculate its L2 Norm using np.linalg.norm(). Then, use vectorization to divide the original array by that norm value.
"""
import numpy as np
a = np.array([3, 6, 33])
norm_val = np.linalg.norm(a)
normalized_a = a / norm_val
print(normalized_a)