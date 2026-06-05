"""
Task 51: Centering Data (Column Demean)
In data science, we often "center" our data by subtracting the average value so the data has a mean of 0.
Question: 1. Create a 3×3 matrix of random numbers between 1 and 10 using np.random.randint(1, 10, size=(3,3)).
2. Calculate the mean of each column by using .mean(axis=0).
3. In one line, subtract those column means from your original matrix using broadcasting.
"""
import numpy as np
a=np.random.randint(1,10,size=(3,3))
print(np.mean(a,axis=0),np.subtract())