# ---------------------------------------------------------
# 🧬 THE SOLO CHALLENGE: THE DUNDER MERGER (HARD)
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You are building a custom tracker for your small-cap mutual funds. 
# Instead of writing clunky merge functions, you want to be able to 
# combine two separate fund accounts by simply adding them together 
# using the standard '+' math operator.
# 
# THE REQUIREMENTS:
# 
# 1. THE CLASS:
#    - Create a class named 'MutualFund'.
#    - Build an __init__ method that takes 'name' (str) and 'balance' (int).
# 
# 2. THE STRING MAGIC:
#    - Build the __str__ magic method. 
#    - It must return an f-string: f"{self.name} Fund: ₹{self.balance}"
# 
# 3. THE MATH MAGIC:
#    - Build the __add__ magic method. It takes 'self' and 'other'.
#    - Inside it, create a new combined name: f"{self.name} & {other.name}"
#    - Create a new combined balance: self.balance + other.balance
#    - RETURN a brand new MutualFund object using those combined stats.
# 
# 4. THE EXECUTION:
#    - Outside the class, create Fund A: bandhan = MutualFund("Bandhan Small Cap", 15000)
#    - Create Fund B: parag = MutualFund("Parag Parikh Flexi", 25000)
#    - Create the merged fund using pure math: mega_fund = bandhan + parag
#    - Print 'mega_fund'.
# 
# EXPECTED OUTPUT:
# Bandhan Small Cap & Parag Parikh Flexi Fund: ₹40000
# ---------------------------------------------------------
class mutualfund:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __str__(self):
            return f"{self.name} Fund: ₹{self.balance}"
    def __add__(self, other):
        new_name = f"{self.name} & {other.name}"
        new_balance = self.balance + other.balance
        return mutualfund(new_name, new_balance)
bandhan=mutualfund("Bandhan Small Cap",15000)
parag=mutualfund("Parag Parikh Flexi",25000)
mega_fund=bandhan+parag
print(mega_fund)