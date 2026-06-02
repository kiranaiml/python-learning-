#💻 Question 8: The "Even" Slice
#This tests your ability to "jump" through an array using the step parameter.
#The Task:
#Create a 1D array of numbers from 0 to 9: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#The Goal:
#Use Slicing to print only the numbers at the even indices (0, 2, 4, 6, 8).
import numpy as np
arr=np.array([0,1,2,3,4,5,6,7,8,9])
print(arr[0:10:2])