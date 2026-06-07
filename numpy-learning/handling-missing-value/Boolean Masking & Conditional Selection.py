"""
1.
Print all values greater than 50.
2.
Print all values less than 40.
3.
Print all even numbers.
4.
Print all odd numbers.
5.
Count how many values are greater than 50.
6.
Find the indices of values greater than 50.
7.
Create a new array containing only values between 30 and 80.
8.
Replace all values greater than 80 with 999.
"""
import numpy as np

data = np.array([
    12, 25, 38, 41, 50,
    63, 74, 85, 96, 100
])

print(data[data > 50])
print(data[data < 40])
print(data[data % 2 == 0])
print(data[data % 2 != 0])
print(np.size(data[data > 50]))


n = data[(data > 30) & (data < 80)]
print(n)
print(np.where(data > 50))

data[data > 80] = 999
print(data)