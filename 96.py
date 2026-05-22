# 1. The Base Class
class Investment:
    def __init__(self, fund_name):
        self.fund_name = fund_name
        self._principal = 0  # Protected variable
        
    def deposit(self, amount):
        if amount < 0:
            print("❌ Invalid deposit!")
        else:
            self._principal += amount
            print(f"✅ Deposited ₹{amount} into {self.fund_name}.")
            
    def project_value(self):
        # Base investment just returns the exact money put in
        return self._principal

# 2. Inheritance & Polymorphism
class SmallCapFund(Investment):
    # Polymorphism: Overwriting the projection method
    def project_value(self):
        # 15% Return
        return self._principal * 1.15 

class SilverETF(Investment):
    # Polymorphism: Overwriting the projection method
    def project_value(self):
        # 10% Return
        return self._principal * 1.10 

# 3. Composition & The Loop
class Portfolio:
    def __init__(self, investor_name):
        self.investor_name = investor_name
        # Composition: The portfolio owns a list of other objects!
        self.fund_list = [] 
        
    def add_fund(self, fund):
        self.fund_list.append(fund)
        
    def show_summary(self):
        grand_total = 0
        print(f"📊 {self.investor_name}'s Portfolio Summary:")
        
        # The Loop: Talking to every object in the list
        for fund in self.fund_list:
            # Polymorphism in action! The loop doesn't know if it's a Small Cap or Silver ETF.
            # It just presses the `project_value()` button and trusts the object to do its own math.
            projected = fund.project_value()
            grand_total += projected
            print(f"   -> {fund.fund_name}: ₹{projected}")
            
        print(f"🏦 Total Portfolio Projected Value: ₹{grand_total}")


# --- 🎬 The Execution Block ---
if __name__ == "__main__":
    # 1. Create the Master Portfolio
    my_portfolio = Portfolio("Kiran")
    
    # 2. Create the Individual Funds
    fund1 = SmallCapFund("Bandhan Small Cap")
    fund2 = SilverETF("Tata Silver")
    fund3 = SmallCapFund("Parag Parikh Flexi")
    
    # 3. Add funds to the Portfolio
    my_portfolio.add_fund(fund1)
    my_portfolio.add_fund(fund2)
    my_portfolio.add_fund(fund3)
    
    # 4. Deposit daily SIPs
    print("--- Monthly Deposits ---")
    fund1.deposit(500)
    fund2.deposit(500)
    fund3.deposit(500)
    
    print("\n--- Year End Projection ---")
    # 5. Run the Loop!
    my_portfolio.show_summary()