""""
# Task 1:
# Print the array in ascending order.

# Task 2:
# Print the array in descending order.

# Task 3:
# Find all unique values.

# Task 4:
# Count how many unique values are present.

# Task 5:
# Find the index positions that would sort the array.

# Task 6:
# Find the largest value.

# Task 7:
# Find the second largest value.

# Task 8:
# Find the smallest value.

"""
# Concept Name: NumPy Sorting & Unique Values

import numpy as np

data = np.array([
    45, 12, 78, 12, 34,
    78, 90, 23, 45, 67
])

print(np.sort(data))
print(np.sort(data)[::-1])
print(np.unique(data))
print(np.size(np.unique(data)))
print(np.max(data))
print(np.min(data))
print(np.argsort(data))
print(np.sort(data)[-2])
