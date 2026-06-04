"""

💻 Task 19: Splitting (Horizontal)
The Array: Create a 2x4 array (2 rows, 4 columns).
The Goal: Use np.hsplit to divide it into four separate 2x1 arrays.
Target Output: A list containing four small vertical arrays.
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.hsplit(arr, 2))