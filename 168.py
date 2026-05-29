# ---------------------------------------------------------
# 🟡 THE SOLO CHALLENGE: THE FILTER (MEDIUM)
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You have a list of stock prices, but your algorithm only 
# cares about expensive stocks. You need to filter out 
# everything that is ₹200 or less.
# 
# THE DATA:
# prices = [100, 250, 400, 50, 300]
# 
# THE REQUIREMENTS:
# 
# 1. THE FILTER FUNCTION:
#    - Create a new variable called 'expensive_stocks'.
#    - Use filter() and a 'lambda' function on the 'prices' list.
#    - The lambda function should check if a number (x) is GREATER THAN (>) 200.
# 
# 2. THE CONVERSION:
#    - Just like map(), filter() returns a raw object. 
#    - Wrap your filter() code inside list() so you can see it!
# 
# 3. THE OUTPUT:
#    - Print the 'expensive_stocks' list.
# 
# EXPECTED OUTPUT:
# [250, 400, 300]
# ---------------------------------------------------------
prices=[100,250,400,50,300]
expesive_stocks=filter(lambda x:x>200,prices)
print(list(expesive_stocks))