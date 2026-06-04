"""
💻 Task 13: Stacking (Depth)
The Goal: Use np.dstack to combine [1, 2, 3] and [4, 5, 6].
Note: Watch the output brackets closely—this creates a 3D effect (depth).
"""
import numpy as np
ah=np.array([1,2,3])
av=np.array([4,5,6])
print(np.dstack((ah,av)))