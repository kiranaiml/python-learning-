#"Smart ATM Withdrawal"
print("\n____ATM WITHDRAWAL____")
current_balance=int(input("current balance:  "))
Withdrawal_amount=float(input("withdrawal ammount: "))
remaining_balance=round(current_balance-Withdrawal_amount)
if Withdrawal_amount > current_balance:
    print("Transcation Failed: Insufficient funds.")
elif Withdrawal_amount==current_balance:
    print("Transcation Successfull: Your account is now empty!")
elif Withdrawal_amount<current_balance and Withdrawal_amount>50000:
    print("Transcation Successfull: Large Withdrawal detected. Please take your cash")
else : 
    print(f"Transcation Successfull! New balance: ${remaining_balance}")