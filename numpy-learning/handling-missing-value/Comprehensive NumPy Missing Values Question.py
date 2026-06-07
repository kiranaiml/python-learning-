"""

import numpy as np

data = np.array([
    10, np.nan, 25, 30, np.nan,
    15, 40, np.nan, 50, 20
])

# Perform the following tasks:

# 1. Check whether the array contains missing values.
# 2. Find the indices of all missing values.
# 3. Count the total number of missing values.
# 4. Extract only the non-missing values.
# 5. Calculate:
#    a) Mean
#    b) Median
#    c) Maximum
#    d) Minimum
#    (Ignoring missing values)
# 6. Replace missing values with:
#    a) Mean
#    b) Median
# 7. Create a new array with all missing values removed.
# 8. Find the percentage of missing values.
# 9. Create a boolean mask showing missing-value positions.
# 10. Print all results clearly.
"""
import numpy as np
data = np.array([
    10, np.nan, 25, 30, np.nan,
    15, 40, np.nan, 50, 20
])

print("Indice value.1:", data[1])
print("Indice value.2:", data[4])
print("Indice value.3:", data[7])

print("The sum of missing value:", np.sum(np.isnan(data)))

data1 = data[~np.isnan(data)]

print("Mean:", np.mean(data1))
print("Median:", np.median(data1))
print("The Data Max num:", np.max(data1))
print("The Data min num:", np.min(data1))

value = np.nanmean(data)
print("The Missing num Mean:", value)

value2 = np.nanmedian(data)
print("The Missing num Median:", value2)

percentage = np.sum(np.isnan(data)) / len(data) * 100
print("The Missing Value Percentage:", percentage)

print("Boolean Mask:", np.isnan(data))