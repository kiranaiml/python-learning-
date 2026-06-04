"""
💻 Task 3: The "Cleanup" (Delete)
Now, let’s try the opposite. Sometimes you have "garbage" data in the middle of your array that needs to be removed.
The Array: arr = np.array([10, 20, 999, 30, 40])
The Goal: Use np.delete to remove the number 999.
The Requirement: You must tell np.delete the index (the position) where 999 is sitting.
"""
import numpy as np
arr=np.array([10,20,999,30,40])
print(np.delete(arr,2))