while True:
    print("\n--- 📈 The Wealth Architect ---")
    user_input = input("Enter your monthly investment (or type 'exit' to quit): ").lower()
    
    if user_input == "exit" or user_input == "break":
        print("Shutting down the financial terminal...")
        break
        
    else:
        monthly_inv = float(user_input) 
        return_rate = float(input("Enter your expected annual return % (e.g. 15): "))
        years = int(input("Enter the number of years for this strategy: "))
        total_amount = 0
        yearly_inv = monthly_inv * 12
        total_invested_cash = yearly_inv * years
        for i in range(years):
            total_amount = total_amount + yearly_inv
            growth = total_amount * (return_rate / 100)
            total_amount = total_amount + growth
        print("\n--- 📊 Projection Results ---")
        print(f"Total Cash Invested: ₹{total_invested_cash}")
        print(f"Total Wealth Created: ₹{total_amount}")
        print("-----------------------------\n")