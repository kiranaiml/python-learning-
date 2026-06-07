"""

Tasks:
Generate 5 random integers between 1 and 100.
Generate a 3×3 array of random integers between 10 and 50.
Generate 5 random decimal numbers between 0 and 1.
Set a random seed and generate 5 random integers.
Randomly choose 3 values from:
"""
import numpy as np

numbers = np.array([
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100
])
print(np.random.randint(1,100))
print(np.random.randint(10,50,(3,3)))
print(np.random.rand(10))
print(np.random.seed(13))