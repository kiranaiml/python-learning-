#The Daily SIP Allocator
total_capital=0
def allocate_funds(fund_name,daily_amount,days):
    global total_capital
    total_contribution=daily_amount*days
    total_capital += total_contribution
    print(f"Allocated to {fund_name} | Daily SIP:₹{daily_amount} | Total Contribution: ₹{total_contribution}")
allocate_funds("Bandhan Small Cap",daily_amount=500,days=15)
allocate_funds("Tata Silver ETF",daily_amount=200,days=15)
print(f"\nTotal Capital Invested: ₹{total_capital}")