"""
💻 Task 23: Deleting (Multiple)
The Goal: Take the array [10, 20, 30, 40, 50].
The Action: Use np.delete to remove the elements at index 1 and index 3 in one go.
Target Output: [10 30 50]
"""
import numpy as np
a=np.array([10,20,30,40,50])
print(np.delete(a,(1,3)))