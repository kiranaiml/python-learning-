"""
Task 50: The Final Shape Challenge
Question: Reshape a 1D array np.array([1, 2, 3]) to a shape of (3,1) and multiply it by a 1D array np.array([10, 20]).
The Goal: Write the code, run it, and tell me what the resulting shape of the output matrix is.
"""
import numpy as np
a=np.array([1,2,3]).reshape(3,1)
b=np.array([10,20])
result=a*b
print(result)
