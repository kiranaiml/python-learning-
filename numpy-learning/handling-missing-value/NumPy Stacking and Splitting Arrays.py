"""

Join A and B into a single array.
Print the shape of the new array.
Find the total number of elements.
Find the maximum value.
Find the minimum value.
"""


import numpy as np

A = np.array([10, 20, 30])
B = np.array([40, 50, 60])
value=np.concatenate((A,B))
print(value)
print(np.shape(value))
print(np.size(value))
print(np.max(value))
print(np.min(value))