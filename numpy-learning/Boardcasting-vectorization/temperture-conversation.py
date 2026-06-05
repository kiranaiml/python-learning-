"""
Task 54: Temperature Conversion
Let's see how you handle a multi-step algebraic formula on an entire array.
Question: Create an array of 5 temperatures in Celsius: [0, 10, 20, 30, 40]. Use one vectorized line of code to convert them all to Fahrenheit using the formula:
F=C× 
5
9
​	
 +32
"""
import numpy as np
a=np.array([0,3,5,630,43,80])
f=(a*5/9)+35
print(f)