# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE PORTFOLIO LOOP
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are managing a financial dashboard. You need to prove 
# that you can store multiple custom objects inside a standard 
# Python list, and use a loop to update all their data at once.
# 
# SYSTEM REQUIREMENTS:
# 1. Create a class named `Asset`.
# 2. In the setup engine, accept `fund_name` and `value`.
# 3. Create a method `add_profit(self, amount)` that adds 
#    the amount to the object's value.
# 4. Outside the class, build THREE separate objects:
#    - Asset 1: "Small Cap", starting value 5000
#    - Asset 2: "Silver ETF", starting value 2000
#    - Asset 3: "Flexi Cap", starting value 8000
# 5. Put all three of your new objects inside a single Python 
#    list called `my_portfolio`. (Hint: `[asset1, asset2, ...]`)
# 6. Write a `for` loop that iterates through `my_portfolio`.
# 7. INSIDE the loop, call the method to add 500 profit to EVERY asset.
# 8. Write a second `for` loop to print the name and updated 
#    value of each asset using dot notation.
# 
# EXPECTED OUTPUT:
# Small Cap: 5500
# Silver ETF: 2500
# Flexi Cap: 8500
# ---------------------------------------------------------
class asset:
    def __init__(self,fund_name,value):
        self.fund_name=fund_name
        self.value=value
    def add_profit(self,amount):
        self.value+=amount
asset1 = asset("Small Cap", 5000)
asset2 = asset("Silver ETF", 2000)
asset3 = asset("Flexi Cap", 8000)

my_portfolio = [asset1, asset2, asset3]
for asset in my_portfolio:
    asset.add_profit(500) 
for asset in my_portfolio:
    print(f"{asset.fund_name}: {asset.value}")