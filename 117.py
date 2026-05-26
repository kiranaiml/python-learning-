
class SmallCapFund:
    def calculate(self, amount):
        return amount * 1.15
class ETF:
    def calculate(self, amount):
        return amount * 1.12

class FixedDeposit:
    def calculate(self, amount):
        return amount * 1.07
class Crypto:
    def calculate(self, amount):
        return amount * 2.00 
class InvestmentTracker:
    def calculate_returns(self, investment_object, amount):
        return investment_object.calculate(amount)
tracker = InvestmentTracker()
my_etf = ETF()
print(tracker.calculate_returns(my_etf, 500)) 

my_crypto = Crypto()
print(tracker.calculate_returns(my_crypto, 500))