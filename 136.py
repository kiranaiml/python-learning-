# =====================================================================
# 🚀 LEVEL 5: THE UNBREAKABLE OBJECT
# =====================================================================
# 
# YOUR MISSION INSIDE THE withdraw() METHOD:
# 1. try: Convert the requested amount into an integer -> clean_amount = int(amount)
# 2. except ValueError: Print f"Error: '{amount}' is not a valid number!"
# 3. else: Subtract clean_amount from self.balance AND print a success message.
# 4. finally: Print f"Card Returned. Current Balance: ₹{self.balance}"
# =====================================================================

class BankAccount:
    def __init__(self, owner, starting_balance):
        # Setting up the object's internal data
        self.owner = owner
        self.balance = starting_balance

    # This is the action the object can perform!
    def withdraw(self, amount):
        print(f"\n--- Processing ATM Request for {self.owner} ---")
        try:
            clean_amount=int(amount)
        except ValueError:
            print(f"Error: '{amount}' is not a valid number!")
        else:
            self.balance=self.balance-clean_amount
            print("Success")
        finally:
            print(f"Card Returned. Current Balance: ₹{self.balance}")


# --- RUNNING THE PRODUCTION SERVERS ---

# 1. We build your object
my_account = BankAccount("Kiran", 10000)

# 2. We test it with a VALID number
my_account.withdraw(2000)

# 3. We test it with a GLITCHY text string to see if your shield holds!
my_account.withdraw("Five Thousand")