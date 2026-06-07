"""
Task
Create an array that contains:
Some numbers
At least 4 missing values
Then create a new array that contains only the valid numbers (all missing values removed).
What to print
Original array
New array with only valid numbers
Length of the original array
Length of the new array
Don't look up the solution. Try it yourself and send me your code. I'll review:
Correctness
NumPy style
Whether there's a more efficient approach

"""
import numpy as np
a=np.array([np.nan,23,3,45,6,np.nan,56,5,np.nan,45,45,np.nan,4,54,])
b=np.sum(a)
print(a)
print(b)