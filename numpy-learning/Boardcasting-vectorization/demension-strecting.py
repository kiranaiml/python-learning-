"""
ask 46: Dimension Stretching
Question: Create a 2×3 array of any numbers. Create a single-element array containing just [5]. Add them together and print the result.
"""
import numpy as np
a=np.ones((2,3))
b=np.array([5])
ab=a+b
print (ab)