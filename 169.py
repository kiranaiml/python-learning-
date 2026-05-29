# ---------------------------------------------------------
# 🔴 THE SOLO CHALLENGE: THE REDUCER (HARD)
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You have a list of daily expenses. You need to calculate 
# the total amount of money spent using reduce().
# 
# THE DATA:
# expenses = [50, 120, 30, 200]
# 
# THE REQUIREMENTS:
# 
# 1. THE IMPORT:
#    - reduce() is hidden inside Python's functools library. 
#    - You MUST type this at the very top of your file:
#      from functools import reduce
# 
# 2. THE REDUCE FUNCTION:
#    - Create a new variable called 'total_spent'.
#    - Use reduce() on the 'expenses' list.
#    - The lambda function for reduce needs TWO variables (x, y) 
#      because it adds two numbers together at a time:
#      lambda x, y: x + y
# 
# 3. THE OUTPUT:
#    - Print the 'total_spent'. 
#    - (Note: reduce() gives you a normal single number, so you 
#      DO NOT need to wrap it in list() this time!)
# 
# EXPECTED OUTPUT:
# 400
# ---------------------------------------------------------
from functools import reduce
expense=[50,120,30,200]
total_spent=reduce(lambda x,y:x+y,expense)
print(total_spent)