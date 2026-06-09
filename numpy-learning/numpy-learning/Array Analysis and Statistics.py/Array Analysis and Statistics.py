"""

All marks in ascending order
All marks in descending order
Highest mark
Lowest mark
Unique marks
Number of unique marks
Index positions after sorting (argsort)
Second highest mark
Average mark
Total sum of all marks
"""

import numpy as np
import numpy as np

marks = np.array([
    78, 45, 89, 67, 92,
    56, 78, 45, 99, 81
])
print(np.sort(marks))
print(np.sort(marks)[::-1])
print(np.max(marks))
print(np.min(marks))
print(np.unique(marks))
print(np.size(np.unique(marks)))
print(np.argsort(marks))
print(np.sort(marks)[-2])
print(np.average(marks))
print(np.sum(marks))