"""
Task 45: Scalar Broadcasting
Question: Create a 4×4 identity matrix. Multiply the entire matrix by a scalar value of 10 using broadcasting and print the result.
"""
import numpy as np
matrix=np.eye(4)
mult=matrix*10
print(mult)