#"The Ultra-Bank Loan Approved"
customer_name = input("Customer Name: ")
age = int(input("Age: "))
credit_score = int(input("Credit Score: "))
monthly_income = float(input("Monthly Income: "))
loan_amount = float(input("Loan Amount: "))
existing_debt = input("Existing Debt (yes/no): ").lower()

# 1. THE GATEKEEPERS
if age < 21:
    print("SORRY! You must be at least 21.")
elif credit_score < 600:
    print("Loan Denied: Credit score too low.")
elif loan_amount > (monthly_income * 5):
    print("Loan Denied: Debt-to-Income ratio too high.")
else:
    # 2. START THE SNOWBALL (Inside the 'else' so it only runs if approved)
    print("WELCOME!! to Canara Bank.")
    base_rate = 5.0
    
    if credit_score >= 720:
        base_rate -= 1.2
        print(">> Bonus: Excellent Credit (-1.2%)")
        
    if existing_debt == 'yes':
        base_rate += 2.5
        print(">> Penalty: Existing Debt (+2.5%)")
        
    if loan_amount > 50000:
        base_rate += 0.5
        print(">> Surcharge: Large Loan (+0.5%)")

    # 3. CALCULATIONS (Flush to the left wall of this 'else' block)
    interest_total = loan_amount * (base_rate / 100)
    total_payback = round(loan_amount + interest_total, 2)
    
    # ID: Name(2) + First Digit of Credit Score + L
    loan_id = customer_name[0:2].upper() + str(credit_score)[0] + "L"

    # 4. THE RECEIPT
    print("\n" + "="*30)
    print("   CANARA BANK LOAN RECEIPT")
    print("="*30)
    print(f"LOAN ID:      {loan_id}")
    print(f"NAME:         {customer_name}")
    print(f"INTEREST RATE: {round(base_rate, 1)}%")
    print(f"LOAN AMOUNT:   ${loan_amount}")
    print("-" * 30)
    print(f"TOTAL PAYBACK: ${total_payback}")
    print("="*30)
    print("    LOAN STATUS: APPROVED")
    print("="*30)


