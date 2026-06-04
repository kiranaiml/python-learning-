"""
💻 Task 18: Stacking (Column)
Goal: Create two 2x2 arrays and use np.column_stack to join them side-by-side.
"""
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.column_stack((a, b)))