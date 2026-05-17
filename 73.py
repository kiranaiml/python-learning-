# The Global State
portfolio_balance = 0

def deposit(amount):
    global portfolio_balance
    portfolio_balance += amount
    print(f"₹{amount} successfully deposited.")

def project_wealth():
    global portfolio_balance
    
    five_year_goal = portfolio_balance * 1.15
    print(f"Estimated 5-year value at 15% return: ₹{five_year_goal}")

while True:
    print("\n1. Deposit Daily SIP | 2. View Projection | 3. Exit")
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        daily_sip = int(input("Enter your daily SIP amount: "))
        deposit(daily_sip)
        
    elif user_input == "2":
        project_wealth()
        
    else:
        print("System shutting down...")
        break