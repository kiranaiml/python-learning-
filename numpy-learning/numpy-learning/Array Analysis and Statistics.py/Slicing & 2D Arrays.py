"""
First row
Second column
Last row
Center value (50)
First two rows
Last two columns
Sum of all values

"""

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data[0:1])
print(data[:,1])
print(data[2:3])
print(data[1,1])
print(data[:2])
print(data[:,1:])
print(np.sum(data))