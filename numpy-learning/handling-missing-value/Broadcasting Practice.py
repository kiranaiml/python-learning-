"""
🔥 Tasks:
1. Add 10 to all elements
2. Multiply all elements by 2
3. Subtract 5 from all elements
4. Divide all elements by 10
5. Add this row-wise array:
"""
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data+10)
print(data*2)
print(data-5)
print(data/10)
print(data + [1, 2, 3])