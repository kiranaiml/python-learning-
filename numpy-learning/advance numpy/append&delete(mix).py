"""
Task 10: Append & Delete (Mixed)
The Challenge: Start with an array [1, 2, 3]. In one single line of code inside a print() function:
Append [4, 5, 6] to it.
From that specific result, delete the element at index 0.
"""
import numpy as np
arr=np.array([1,2,3,4])
print(np.delete(np.append(arr,[5,6,7]),0))