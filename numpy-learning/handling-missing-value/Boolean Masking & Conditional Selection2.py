"""
Tasks
Print all values greater than 60.
Print all values less than 50.
Print all even values.
Print all odd values.
Count how many values are greater than 60.
Find the indices of values greater than 60.
Create a new array containing values between 30 and 90.
Replace all values greater than 90 with 500.
"""
import numpy as np

data = np.array([
    15, 28, 35, 42, 57,
    64, 71, 88, 95, 100
])
print(data[data>60])
print(data[data<50])
print(data[data %2==0])
print(data[data %2!=0])
print(np.size(data[data>60]))
print(np.where(data > 60))
d=data[(data>30) & (data<90)]
print(d)
data[data>90]=500
print(data)