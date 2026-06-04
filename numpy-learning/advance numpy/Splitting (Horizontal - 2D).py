"""
💻 Task 19: Splitting (Horizontal - 2D)
To see the real power of horizontal vs vertical splitting, try it on a 2D grid.
The Array: Create a 2x4 array: np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
The Goal: Use np.hsplit to divide it into four separate 2x1 arrays.
"""
import numpy as np
arr=np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.hsplit(arr,2))