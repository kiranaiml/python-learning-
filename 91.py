#the fintech SIP investment engine
class mutualfund:
    def __init__(self,fund_name,nav_price,wallet_balance=0):
        self.fund_name = fund_name
        self.nav_price = nav_price
        self.wallet_balance = wallet_balance
        self.portfolio = {}

    def invest_sip(self,fund_object,investment_amount):
        if self.wallet_balance >= investment_amount:
            units_bought = round(investment_amount / fund_object.nav_price, 2)
            self.wallet_balance -= investment_amount

            if fund_object.fund_name in self.portfolio:
                self.portfolio[fund_object.fund_name] += units_bought
            else:
                self.portfolio[fund_object.fund_name] = units_bought

            print(f"✅ {self.fund_name} invested ₹{investment_amount} into {fund_object.fund_name}. Units acquired: {units_bought:.2f}")
        else:
            print(f"❌ Insufficient wallet balance: need ₹{investment_amount}, have ₹{self.wallet_balance}")

    def show_portfolio(self):
        print(f"--- {self.fund_name}'s Investment Portfolio ---")
        print(f"Wallet Balance: ₹{self.wallet_balance}")
        for fund_name, units in self.portfolio.items():
            print(f"- {fund_name}: {units:.2f} units")


if __name__ == '__main__':
    investor = mutualfund('Kiran', 0, wallet_balance=2000)
    bandhan = mutualfund('Bandhan Small Cap Fund', 55.5)
    tata = mutualfund('Tata Silver ETF', 120)

    investor.invest_sip(bandhan, 500)
    investor.invest_sip(tata, 1000)
    investor.invest_sip(bandhan, 500)
    investor.show_portfolio()