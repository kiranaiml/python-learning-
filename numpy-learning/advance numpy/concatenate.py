"""
💻 Task 4: The "Double Team" (Concatenate)
Joining two arrays is like connecting train cars.
The Arrays: a = np.array([1, 2, 3]) and b = np.array([4, 5, 6])
The Goal: Use np.concatenate to join them into one long array.
The Rule: You must put a and b inside a tuple (extra parentheses) like this: (a, b)
"""
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate((a,b)))