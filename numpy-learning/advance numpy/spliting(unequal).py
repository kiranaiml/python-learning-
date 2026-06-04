"""
💻 Task 14: Splitting (Unequal)
The Goal: Create a 1D array with 6 elements.
The Action: Use np.array_split to divide it into 4 parts.
"""
import numpy as np
arr=np.arange(1,7)
print(np.array_split(arr,4))