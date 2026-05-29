import datetime

# 1. THE DECORATOR
def log_transaction(func):
    # The wrapper takes any arguments (*args) that the original function needs
    def wrapper(*args, **kwargs):
        
        # --- WRITE YOUR DECORATOR LOGIC HERE ---
        time=datetime.datetime.now()
        print(f"🔒 LOG: {func.__name__} was called at {time}")
        # Hint 1: Get the current time using datetime.datetime.now()
        # Hint 2: Print something like: f"🔒 LOG: {func.__name__} was called at {time}"
        
        
        # Finally, we run the actual function that was passed in!
        return func(*args, **kwargs)
        
    return wrapper

# 2. THE CORE FUNCTIONS (Notice the @ syntax!)
@log_transaction
def deposit(amount):
    print(f"✅ Successfully deposited ₹{amount}\n")

@log_transaction
def withdraw(amount):
    print(f"✅ Successfully withdrew ₹{amount}\n")

# 3. THE EXECUTION
print("--- BANKING SYSTEM INITIATED ---\n")
deposit(500)
withdraw(150)