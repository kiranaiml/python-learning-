"""
💻 Task 7: The "Multi-Delete"
The Array: arr = np.arange(10) (This gives you [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
The Goal: Use np.delete to remove the numbers at index 0, index 5, and index 9 all at once.
"""
import numpy as np
arr=np.arange(0,10)
print(np.delete(arr,[0,5,9]))