"""
Task 1
Create an array with some numbers and 3 missing values. Find the total number of missing values.
"""
import numpy as np
a=np.array([2,3,np.nan,5,6,np.nan,np.nan,90])
print(np.sum(np.isnan(a)))
