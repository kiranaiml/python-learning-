"""
🔥 Tasks:
1. Print shape of array
2. Reshape into (1, 9)
3. Reshape into (9, 1)
4. Flatten the array
5. Reshape into (3, 3) again
"""
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(np.shape(data))
print(np.reshape(data,(1,9)))
print(np.reshape(data,(9,1)))
print(data.flatten())
print(np.reshape(data,(3,3)))