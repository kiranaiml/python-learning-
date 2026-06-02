#💻 Question 11: The "Corner" Extraction
#This is where you show you can handle 2D data like a pro. We are going to pull a small "box" out of a bigger "box."
#The Task:
#Create a 4x4 array (you can use np.arange(16).reshape(4,4) to make it easy).
#The Goal: Extract the first two rows AND the last two columns.
import numpy as np
arr_2d=np.arange(16)
arr_2d=arr_2d.reshape(4,4)
print(arr_2d[0:2,0:2])