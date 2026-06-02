#Create a 1D array of 10 random numbers. Find the Mean, Median, and Standard Deviation (std).
import numpy as np
arr_1d=np.random.randint(1,101,10)
arr_1d2=np.mean(arr_1d)
arr_1d3=np.median(arr_1d)
arr_1d4=np.std(arr_1d)
print(arr_1d2)
print(arr_1d3)
print(arr_1d4)