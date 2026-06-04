"""
💻 Task 8: The "Column Concatenate"
Now let's join arrays side-by-side. Pay close attention to the shape—these are 2D arrays with one number per row.
Array A: np.array()
Array B: np.array([[4], [5], [6]])
The Goal: Use np.concatenate with axis=1 to join them.
"""
import numpy as np
a=np.array([[1],[2],[3]])
b=np.array([[4],[5],[6]])
print(np.concatenate((a,b),axis=1))