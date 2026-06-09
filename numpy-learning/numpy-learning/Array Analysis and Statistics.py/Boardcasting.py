"""
Print 10 random integers between 1 and 100.
Print a 3×3 random integer array between 1 and 50.
Print one random value from [10, 20, 30, 40, 50].
"""
import numpy as np
print(np.random.randint(1,100,10))
d=np.random.randint(1,50,9)
print(d.reshape(3,3))
d1=[10, 20, 30, 40, 50]
print(np.random.choice(d1))