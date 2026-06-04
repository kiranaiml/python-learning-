"""

💻 Task 15: Concatenation (2D)
The Goal: Join [[1, 2]] and [[3, 4]] along axis=0.
The Rule: Print the result in one line.
"""
import numpy as np
a=np.array([[1,2]])
b=np.array([[3,4]])
print(np.concatenate((a,b),axis=0))