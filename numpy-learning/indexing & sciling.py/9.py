#💻 Question 9: Target the Center
#Create: Use np.eye(5) to make a 5x5 identity matrix (1s on the diagonal, 0s elsewhere).
#Modify: Target the middle element (the center) and change it to 10.
#Print: Let's see the whole matrix.
import numpy as np
arr=np.eye(5)
arr[2,2]=200
print(arr)