#he Task: Create a 1D array of numbers from 1 to 10 and print only the numbers that are greater than 3 AND less than 8 using a single line of code.
import numpy as np
print(np.arange(1, 11)[(np.arange(1, 11) > 3) & (np.arange(1, 11) < 8)])