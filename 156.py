import datetime # NEW TOOL: Gets today's exact date and time!

# 1. TEMPORARY MEMORY (Lists and Variables)
# This holds data while the app is running
transaction_list = []
current_balance = 0.0

# 2. THE MASTER LOOP
while True:
    # 3. THE MAIN MENU (Terminal I/O)
    print("\n" + "="*40)
    print(" 🏦 THE FINANCIAL COMMAND CENTER 🏦 ")
    print("="*40)
    print(f"💰 CURRENT BALANCE: ₹{current_balance}")
    print("-" * 40)
    print("1. Add an Income (Money In)")
    print("2. Add an Expense (Money Out)")
    print("3. View Transaction History")
    print("4. Save History to Hard Drive")
    print("5. EXIT System")
    print("="*40)
    
    # 4. LOGIC & ROUTING (If / Elif / Else)
    choice = input("Enter a command (1-5): ")
    
    if choice == "1":
        # Adding Income
        income=input("Enter your income: ")
        source = input("Where did this income come from?: ")
        amount = float(input("Enter amount: ₹"))
        
        current_balance = current_balance + amount
        
        # Build the receipt string and save it to our List memory
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        receipt = f"[{time_stamp}] 🟢 INCOME: {source} | +₹{amount}"
        transaction_list.append(receipt)
        print("✅ Income recorded successfully!")

    elif choice == "2":
        # Adding Expense
        expense=input("Enter your expense: ")
        item = input("What did you buy?: ")
        amount = float(input("Enter amount: ₹"))
        
        current_balance = current_balance - amount
        
        # Build the receipt string and save it to our List memory
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        receipt = f"[{time_stamp}] 🔴 EXPENSE: {item} | -₹{amount}"
        transaction_list.append(receipt)
        print("✅ Expense recorded successfully!")

    elif choice == "3":
        # Reading Data (The For Loop)
        print("\n--- 📜 TRANSACTION HISTORY ---")
        if len(transaction_list) == 0:
            print("No transactions yet. Add some data!")
        else:
            for transaction in transaction_list:
                print(transaction)
        print("------------------------------")

    elif choice == "4":
        # Permanent Storage (File I/O)
        with open("financial_database.txt", "a") as file:
            file.write(f"\n--- LOG SAVED ON {datetime.datetime.now()} ---\n")
            for transaction in transaction_list:
                file.write(transaction + "\n")
            file.write(f"FINAL BALANCE: ₹{current_balance}\n")
            file.write("-" * 40 + "\n")
            
        print("💾 Success! All data securely backed up to 'financial_database.txt'")

    elif choice == "5":
        # The Escape Hatch
        print("Shutting down the Financial Command Center. Goodbye!")
        break
        
    else:
        # Error Handling
        print("⚠️ Invalid command. Please enter a number between 1 and 5.")