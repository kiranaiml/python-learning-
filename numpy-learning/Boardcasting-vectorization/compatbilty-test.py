"""
Task 49: The Compatibility Test (Intentional Error)
Question: Try to add an array of shape (3, 2) to an array of shape (2, 3). Write the code to run it, and see what kind of error NumPy throws when dimensions are completely incompatible.
"""
import numpy as np
a = np.ones((3, 2))
b = np.ones((2, 3))
print(a + b)