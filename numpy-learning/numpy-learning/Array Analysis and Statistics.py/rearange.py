"""
Randomly rearrange the array.
Print the result.
"""
import numpy as np

data = np.array([1,2,3,4,5,6,7,8,9,10])
np.random.shuffle(data)
print(data)