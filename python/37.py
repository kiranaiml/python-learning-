#"The Apex Global Bank"
name = input("Customer Name: ")

# 1. SETUP (Must be Lists [] to allow changes)
account_ids = ["Checking", "Savings", "Emergency"]
balances = [5000.0, 1200.0, 300.0]

# 2. TRANSACTION MODULE
# Deposit bonus to Checking (Index 0)
balances[0] += 1500  

# Transfer $200 from Savings (Index 1) to Emergency (Index 2)
balances[1] -= 200
balances[2] += 200

# Add Crypto Account
account_ids.append("Crypto")
balances.append(0.0)

# 3. LOGIC & MATH
wealth = sum(balances)

# Determine Membership Status
if wealth > 10000:
    status = "GOLD MEMBER. Investment unlocked."
elif 5000 <= wealth <= 10000:
    status = "SILVER MEMBER. Limited investments."
else:
    status = "STANDARD. Build more savings."

# 4. DATA ANALYTICS
max_bal = max(balances)
min_bal = min(balances)
# Security ID: First 3 of Name + First 2 of Wealth + Last Account Name
security_id = name[0:3].upper() + str(int(wealth))[0:2] + account_ids[-1].upper()

# 5. THE DASHBOARD (Moved outside the IF/ELSE so it always prints)
print("\n" + "="*45)
print("       ▲ THE APEX GLOBAL BANK ▲")
print("="*45)
print(f"HOLDER: {name.title()} | ID: {security_id}")
print(f"STATUS: {status}")
print("-" * 45)
print(f"ACCOUNTS: {account_ids}")
print(f"BALANCES: {balances}")
print("-" * 45)
print(f"TOTAL WEALTH:    ${round(wealth, 2)}")
print(f"HIGHEST BALANCE: ${max_bal}")
print(f"LOWEST BALANCE:  ${min_bal}")
print("="*45)
print("      SECURE . GLOBAL . ELITE")
print("="*45)