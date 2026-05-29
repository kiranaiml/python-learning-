# ---------------------------------------------------------
# 🟢 THE SOLO CHALLENGE: THE MAPPER (EASY)
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You have a list of raw order prices. You need to add a 
# ₹50 shipping fee to every single order using map().
# 
# THE DATA:
# prices = [100, 250, 400, 50]
# 
# THE REQUIREMENTS:
# 
# 1. THE MAP FUNCTION:
#    - Create a new variable called 'final_prices'.
#    - Use map() and a 'lambda' function on the 'prices' list.
#    - The lambda function should take a number (x) and add 50 to it.
# 
# 2. THE CONVERSION:
#    - map() returns a map object. You MUST wrap your 
#      map() code inside list() so it becomes a normal list again!
#      Example: final_prices = list(map( ... ))
# 
# 3. THE OUTPUT:
#    - Print the 'final_prices' list.
# 
# EXPECTED OUTPUT:
# [150, 300, 450, 100]
# ---------------------------------------------------------
prices = [100, 250, 400, 50]
final_price=map(lambda x: x+50,prices)
print(list(final_price))

