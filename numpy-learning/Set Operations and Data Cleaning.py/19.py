#Question 19: The "Axis" Challenge (Advanced)
#This is a core concept for data science. Sometimes you don't want the total sum; you want the sum of just the columns or just the rows.
#axis=0: Operates down the columns (vertical).
#axis=1: Operates across the rows (horizontal).
#The Task:
#Create a 3x3 array of numbers from 1 to 9.
#The Goal: Print the sum of each column (you should get 3 separate numbers).
#The Rule: Use axis=0 inside your np.sum() function.
import numpy as np
print(np.arange(1,10).reshape(3,3).sum(axis=0))