"""
Task 27: Unique
The Goal: Use np.unique() on an array with repeats: [1, 1, 2, 2, 3, 3, 3].
The Result: It should "clean" the array so every number only appears once.
"""
import numpy as np
a=np.array([111,22,11,33,22,4,6,999,000,33,4,0,])
print(np.unique(a))