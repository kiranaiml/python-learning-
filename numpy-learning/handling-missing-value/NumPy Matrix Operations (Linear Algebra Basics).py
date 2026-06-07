"""

🔥 Tasks:
1. Print matrix A and B
2. Find transpose of A
3. Perform element-wise multiplication of A and B
4. Perform matrix multiplication of A and B (dot product)
5. Print shape of A and B
"""
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])
print(A,B)
print(np.transpose(A))
print(A*B)
print(np.dot(A, *B))
print(np.shape(A),np.shape(B))