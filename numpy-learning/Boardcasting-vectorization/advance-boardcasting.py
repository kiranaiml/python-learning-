"""
Task 47: Row and Column Grid Generation
Question: Create a column vector of shape (3, 1) containing the values:
Plaintext
[[1], 
 [2], 
 [3]]
And a row vector of shape (1, 3) containing the values [10, 20, 30]. Add them together and print the result.
"""
import numpy as np
a=np.array([[1],[2],[3]])
b=np.array([[10,20,30]])
value=a+b
print(value)
