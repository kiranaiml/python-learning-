#"The FinTech AI Fraud Engine"
transaction_record = {
    "tx_id": "TXN-9942",
    "user_id": "Kiran_01",
    "safe_locations": ("Mysuru", "Bengaluru"), 
    "risk_profile": {
        "flagged_merchants": {"Crypto_X", "Betting_Hub", "DarkWeb_Store"}, 
        "recent_amounts": [450, 1200, 300] 
    },
    "account_status": "Active"
}
user_place=input("Transaction City: ")
merchent_name=input("Merchant Name: ")
user_amount=int(input("Transaction Amount: "))
transaction_record["risk_profile"]["recent_amounts"].append(user_amount)
if user_place not in transaction_record["safe_locations"] or merchent_name in transaction_record["risk_profile"]["flagged_merchants"]:
    transaction_record["account_status"]="FROZEN - Fraud Detected!"
elif user_amount>50000:
    transaction_record["account_status"]="Pending Manual Review"
else:
    transaction_record["payment_cleared"]=True
    
print("\n"+"="*40)
print(f"\nThe Transaction ID: {transaction_record["tx_id"]}")
print(f"The Total Number of transactions:{len(transaction_record["risk_profile"]["recent_amounts"])}")
print(f"The Final Account Status:{transaction_record["account_status"]}")
print(f"The complete updated:{transaction_record}")
print("\n"+"="*40)