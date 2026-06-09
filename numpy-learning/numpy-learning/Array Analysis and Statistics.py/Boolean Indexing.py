""
"""
Numbers greater than 50
Numbers less than 40
Even numbers
Odd numbers
Count of numbers greater than 50
"""
import numpy as np

data = np.array([12, 45, 67, 23, 89, 34, 90, 56])
print(data[data>50])
print(data[data<40])
print(data[data%2==0])
print(data[data%2!=0])
print(np.sum(data[data>50]))