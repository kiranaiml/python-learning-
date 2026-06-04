"""
💻 Task 22: Stacking (Vertical)
The Goal: Create two 1D arrays of 3 elements each.
The Action: Use np.vstack to stack them on top of each other.
Target Output: A 2x3 2D array.
"""
import numpy as np
a = np.array([1, 2, 5])
b = np.array([9, 0, 6])
print(np.vstack((a, b)))