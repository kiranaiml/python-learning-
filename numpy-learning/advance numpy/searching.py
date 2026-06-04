"""
Task 24: Searching
The Goal: Use np.where() on the array [1, 2, 3, 4, 5] to find the indices where values are greater than 3.
Why it's useful: This is how you find "where" specific data lives in a massive dataset.
"""
import numpy as np
a=np.array([1,2,3,4,5])
print(np.where(a>3))