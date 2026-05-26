from abc import ABC,abstractmethod

class market(ABC):
    @abstractmethod
    def invest_daily(self, amount):
        pass
class bull_market(market):
    def   invest_daily(self, amount):    
            print("Market is booming! Aggressive mode.")
            print(f"Allocating ₹{amount} to Bandhan Small Cap Fund.")
            # ... 100 lines of aggressive risk math ...
class bear_market(market):
    def invest_daily(self, amount):
            print("Market is crashing! Safe mode.")
            print(f"Allocating ₹{amount} to Tata Silver ETF.")
            # ... 100 lines of safe hedging math ...
class normal(market):
    def invest_daily(self, amount):
            print("Market is stable. Balanced mode.")
            print(f"Allocating ₹{amount} to Parag Parikh Flexi Cap.")
            # ... 100 lines of balanced portfolio math ...
class investmentbot:
      def __init__(self,strategy:market):
            self.strategy=strategy

      def set_strategy(self,new_strategy:market):
            self.strategy=new_strategy
      def build_strategy(self,amount:market):
            self.strategy.invest_daily(amount)

print("--- Morning: Bull Market ---")
my_bot = investmentbot(bull_market())
my_bot.build_strategy(500)

print("\n--- Afternoon: Market Crashes! ---")
my_bot.set_strategy(bear_market())
my_bot.build_strategy(500)