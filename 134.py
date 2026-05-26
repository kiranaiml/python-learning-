# =====================================================================
# 🚀 LEVEL 3: THE SIP AUTOMATION BOT (Real-World Project)
# =====================================================================

bank_api_data = [
    {"fund_name": "Bandhan Small Cap", "deposit": 500, "nav": 125.50},
    {"fund_name": "Parag Parikh Flexi Cap", "deposit": 500, "nav": 0}, # 🚨 GLITCH: NAV is 0!
    {"fund_name": "Tata Silver ETF", "deposit": "500", "nav": 75.20},  # 🚨 GLITCH: Deposit is a string!
    {"deposit": 500, "nav": 45.10},                                    # 🚨 GLITCH: Missing fund name!
    {"fund_name": "Nippon India Growth", "deposit": 500, "nav": 90.00}
]

total_successful_investments = 0

print("--- Starting Daily SIP Processing ---\n")

for transaction in bank_api_data:
    try:
        name = transaction["fund_name"]
        units = transaction["deposit"] / transaction["nav"]
    
    except KeyError:
        print ("warning about missing fund name")
    except TypeError:
        print ("warning about bad data types ")
    except ZeroDivisionError:
        print("warning about 0 NAV")
    else:
        total_successful_investments.__add__(1)
        print(f"Bought {units} units of {name}")
print(f"\n--- Processing Complete. Total successful SIPs: {total_successful_investments} ---")