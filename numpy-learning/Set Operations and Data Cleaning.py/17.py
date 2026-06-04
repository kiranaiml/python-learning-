#Question 17: Statistics (Mean & Median)
#Now that you can clean data, let’s analyze it. This is huge for anyone looking into finance or business.
#The Task:
#Create an array of numbers: [10, 20, 30, 40, 50]
#The Goal: In one line, print the Average (Mean) of these numbers.
#The Bonus: In a second line, print the Standard Deviation (use np.std).
import numpy as np
arr=np.array([10,20,30,40,50])
print(np.mean(arr))
print(np.std(arr))