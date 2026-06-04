"""
💻 Task 11: Splitting (Vertical)
The Goal: Create a 4x4 array of zeros and use np.vsplit to divide it into two equal parts.
Target Output: Two separate 2x4 arrays within a list.
"""
import numpy as np
arr = np.zeros((4, 4)) 
print(np.vsplit(arr, 2))