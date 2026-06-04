"""
💻 Task 17: Inserting (Multiple Positions)
Goal: Start with a 3-element array. Use np.insert to add the value 100 at index 0 and index 2 at the same time.
"""
import numpy as np
arr=np.array([1,2,3])
print(np.insert(arr,[0,2],100))