"""
💻 Task 26: Filtering
The Goal: Get the actual values that meet a condition, not just their index.
The Action: Create an array [1, 2, 3, 4] and use a Boolean Mask: print(arr[arr > 2]).
The Difference: np.where tells you where the treasure is; Filtering actually grabs the treasure for you.
"""
import numpy as np
a=np.array([1,2,3,4])
print(a[a>2])