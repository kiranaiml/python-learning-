#💻 Question 10: The Reverse
#This is a classic Python and NumPy trick. It uses the "Step" part of slicing.
#The Task:
#Create an array: [1, 2, 3, 4, 5, 6]
#The Goal:
#Print it in reverse: [6, 5, 4, 3, 2, 1] using only one line of slicing.
import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr[::-1])