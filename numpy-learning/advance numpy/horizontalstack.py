"""
💻 Task 31: Horizontal Stack (Review)
The Goal: Join [1, 2] and [3, 4] side-by-side using np.hstack.
The Rule: Remember the tuple syntax (( )).
"""
import numpy as np
a=np.array([[1,3],[4,5]])
b=np.array([[2,9],[6,8]])
print(np.hstack((a,b)))