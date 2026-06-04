"""
💻 Task 2: The "Mid-Array Surgery" (Insert)
Now let's see if you can place a number exactly where it belongs without appending to the end.
The Array: [10, 20, 40, 50]
The Goal: Use np.insert to put the number 30 at index 2.
The Rule: One line for the print statement.
"""
import numpy as np
arr=np.array([10,20,40,50])
print(np.insert(arr,2,30))