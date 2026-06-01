# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE WITHDRAWAL LOGIC
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are building the backend for a mutual fund app. You need 
# a custom object that uses logic to check if a user has enough 
# money BEFORE allowing them to make a withdrawal.
# 
# SYSTEM REQUIREMENTS:
# 1. Create a class named `InvestmentFund`.
# 2. In the setup engine, accept `fund_name` and `balance`.
# 3. Create a method called `withdraw(self, amount)`.
# 4. INSIDE the method, write an `if / else` statement:
#    - IF the `amount` is greater than the object's `balance`, 
#      print exactly: "Transaction Denied". (Do not change the balance).
#    - ELSE, subtract the `amount` from the object's `balance`.
# 5. Outside the class, build a new object for "Parag Parikh Flexi Cap" 
#    with a starting balance of 5000.
# 6. Call the `withdraw` method to attempt a withdrawal of 6000.
# 7. Call the `withdraw` method to attempt a withdrawal of 1000.
# 8. Print the fund's name and its final balance on separate 
#    lines using dot notation.
class investmentfund:
    def __init__(self,fund_name,balance):
        self.fund_name=fund_name
        self.balance=balance
    def withdraw(self,amount):
        if amount>self.balance:
            print("Transcation denied")
        else:
            print("Withdrawal is successfull")
            self.balance-=amount
my_invest=investmentfund("Parag Parikh Flexi Cap",5000)
my_invest.withdraw(6000)
my_invest.withdraw(500)
print(f"Fund name: {my_invest.fund_name}\nFinal balance : {my_invest.balance}")
