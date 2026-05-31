# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE SIP TRACKER
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You have a record of your monthly SIP deposits for the year. 
# Sometimes you invested the standard amount, sometimes you invested 
# extra, and sometimes you missed a month (recorded as 0). 
# You need a system to analyze this data.
# 
# THE INPUT DATA:
# deposits = [500, 500, 0, 500, 1500, 0, 500, 500]
# 
# SYSTEM REQUIREMENTS:
# 1. Calculate the total amount of money invested.
# 2. Count exactly how many months a successful deposit was made 
#    (any month where the amount was greater than 0).
# 3. Print both the total amount and the number of successful months.
# 
# EXPECTED OUTPUT:
# Total Invested: 4500
# Successful Months: 6
# ---------------------------------------------------------
deposits=[500,500,0,500,1500,0,500,500]
total_inveted=0
successfull_month=0
for total_amount in deposits:
    if total_amount>0:
        successfull_month+=1
        total_inveted+=total_amount
print(f"total invested: {total_inveted}\n successful month:{successfull_month}")