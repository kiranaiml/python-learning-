"""
Task 55: The Multiplier Grid (Grand Finale!)
Question: Use broadcasting to create a 10×10 multiplication table (from 1 to 10) in just two lines of code.
Core Idea: Think about how you multiplied a (3, 1) column array by a (2,) row array in Task 50 to get a grid. You want to do that exact same thing, but with numbers from 1 to 10.
"""
import numpy as np

a=np.arange(1,11).reshape(10,1)
b=np.arange(1,11)
print(a*b)