#Create a 4x4 array of random integers between 1 and 100, then use np.where to replace all values greater than 50 with the number 99 and all other values with 0.
import numpy as np
arr = np.where(np.random.randint(1, 101, (4, 4)) > 50, 99, 0)

print(arr)