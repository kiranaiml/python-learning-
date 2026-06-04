#💻 Question 18: Sum and Product
#Before we move to the next major concept, let's look at how to squash an array into a single total value.
#The Task: 1. Create a 2D array (2x3) with any numbers you like.
#2. The Goal: Use np.sum to find the total of all numbers in the array.
#3. The Twist: See if you can find the np.prod function to multiply all the numbers together.
import numpy as np
arr = np.random.randint(1, 11, (2, 3))
print(np.sum(arr))
print(np.prod(arr))