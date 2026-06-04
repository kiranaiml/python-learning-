"""
Task 1: The "Append & Sort"
Create a 1D array with these values: [40, 10, 20]
The Goal: Use np.append to add the values [50, 30] to the end of that array.
The Final Step: Print the sorted version of this new array.
"""
import numpy as np
arr=np.array([40,50,60])
print(np.sort(np.append(arr,[50,30])))