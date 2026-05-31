# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE SIP TRACKER
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are building a backend system to track daily Systematic 
# Investment Plans (SIP). You need a custom blueprint to store 
# the details of individual investments.
# 
# SYSTEM REQUIREMENTS:
# 1. Create a class named `SIP_Account`.
# 2. It must require two pieces of data when initialized: 
#    the fund name and the daily deposit amount.
# 3. Store those two pieces of data inside the object.
# 4. Outside the class, build a new object using the fund name 
#    "Small Cap" and a daily deposit of 500. Save it to a variable.
# 5. Print both pieces of data directly from your object.
# 
# EXPECTED OUTPUT:
# Fund: Small Cap
# Daily Deposit: 500
# ---------------------------------------------------------
class sip_account:
    def __init__(self,fund_name,daily_deposit):
        self.fund_name=fund_name
        self.daily_deposit=daily_deposit
my_sip=sip_account("small cap",500)
print(my_sip)