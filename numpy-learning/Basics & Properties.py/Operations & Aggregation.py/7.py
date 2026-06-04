#n the last question, you found the sum. Now, let's find a specific position.
#The Task:
#Create this 1D array: [15, 45, 12, 89, 34]
#The Goal:
#Find the Index (the position number) of the maximum value.
import numpy as np
arr_1d=np.array([15,45,12,89,34])
arr=np.argmax(arr_1d)
print(arr)