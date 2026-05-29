# 1. THE BLUEPRINT (The Class)
class BankAccount:
    
    # The Setup: Runs when a new account is created
    def __init__(self, owner_name, starting_balance):
        self.owner = owner_name
        self.balance = starting_balance
        print(f"🏦 Account created for {self.owner} with ₹{self.balance}")

    # Action 1: Deposit
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"🟢 Deposited ₹{amount}. New Balance: ₹{self.balance}")

    # Action 2: Withdraw (YOUR TURN!)
    def withdraw(self, amount):
        if amount<=self.balance:
         self.balance-=amount
         print("Your payment is successful")
        else:
         print("Insuffeceint payment")
        # --- WRITE YOUR LOGIC HERE ---
        # Hint 1: Check if amount is less than or equal to self.balance
        # Hint 2: If yes, subtract it and print success.
        # Hint 3: If no, print an error message.
         pass # Delete this 'pass' when you write your code


# 2. THE EXECUTION (Using the factory to build objects)
print("--- FINTECH ENGINE START ---")

# We create two completely separate accounts!
kiran_account = BankAccount("Kiran", 1000)
business_account = BankAccount("Startup LLC", 50000)

# We use the built-in methods
kiran_account.deposit(500)

# Testing your withdraw method!
kiran_account.withdraw(200)   # Should succeed
kiran_account.withdraw(9999)  # Should fail and print error