# 1. THE BLUEPRINT
class DailySIP:
    def __init__(self, fund_name):
        self.fund_name = fund_name
        # These start at 0 automatically for every new SIP!
        self.total_invested = 0
        self.days_completed = 0

    # Notice how this is INDENTED to live inside the class
    def process_market_data(self, data):
        match data:
            case {"status": "market_open", "nav": price}:
                self.total_invested += 500
                self.days_completed += 1
                print(f"✅ Invested ₹500 in {self.fund_name} at NAV {price}. Total invested: ₹{self.total_invested}")
                
            case {"status": "market_closed", "reason": reason}:
                print(f"⏸️ Investment skipped. Reason: {reason}")
                
            case _:
                print("⚠️ Error: Invalid market signal.")


# 2. THE EXECUTION
print("--- 5-YEAR WEALTH ENGINE INITIATED ---\n")

# We create the object (only need to pass the name!)
my_sip = DailySIP("Parag Parikh Flexi Cap")

# The data stream MUST be dictionaries so your 'match' can read them
exchange_feed = [
    {"status": "market_open", "nav": 75.50},
    {"status": "market_closed", "reason": "Weekend"},
    {"status": "market_open", "nav": 76.10},
    {"error": "connection_timeout"}
]

# Send each dictionary into the engine, one by one
for daily_signal in exchange_feed:
    my_sip.process_market_data(daily_signal)

# Print the final memory of the object
print(f"\n📊 SUMMARY: {my_sip.days_completed} days completed. Total: ₹{my_sip.total_invested}")
                        