# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE DISCOUNT ENGINE
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are running a store and having a massive 20% off sale. 
# Instead of doing the math manually for every single customer, 
# you need to build a reusable tool (a Function) that takes 
# ANY price, automatically removes 20%, and returns the final cost.
# 
# SYSTEM REQUIREMENTS:
# 1. Define a function named `apply_discount` that takes exactly 
#    one parameter: `price`.
# 2. Inside the function, calculate the discount amount (price * 0.20) 
#    and subtract it from the original price to get the final cost.
# 3. Use the `return` keyword to send the final cost back out.
# 4. OUTSIDE the function, test your new tool! Call the function 
#    twice: once passing in the number 500, and once passing in 1500. 
# 5. Print both results.
# 
# EXPECTED OUTPUT:
# 400.0
# 1200.0
# ---------------------------------------------------------
def apply_discount(price):
    final_cost = price - (price * 0.20)
    return final_cost
print(f"Final cost: {apply_discount(500)}")
print(f"Final cost: {apply_discount(1500)}")