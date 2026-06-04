#Create this specific 2D array: [[30, 10, 20], [60, 40, 50], [90, 70, 80]]
#The Goal: In one line, sort the entire array and then flatten it so it becomes a simple 1D list from 10 to 90.
import numpy as np
arr=np.array([[30, 10, 20], [60, 40, 50], [90, 70, 80]])
print(np.sort(arr).flatten())