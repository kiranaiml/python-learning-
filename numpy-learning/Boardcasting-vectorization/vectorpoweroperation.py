"""
Task 43: Vectorized Power Operation
Question: Create two arrays: a = np.array([1, 2, 3]) and b = np.array([4, 5, 6]). Use a single vectorized operation to find a 
b
  (each element in a raised to the power of the corresponding element in b).
"""
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.power(a,b))