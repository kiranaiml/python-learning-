#Create a 1D array of numbers from 1 to 20.
#Find all the odd numbers in that array.
#Replace all those odd numbers with -1
import numpy as np 
arr=np.arange(1,21)
arr[arr%2!=0]=-1
print(arr)