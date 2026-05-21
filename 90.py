#The upi payment engine
class bankaccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
    def send_money(self,reciver_account,amount):
        # Transfer `amount` from this account to `reciver_account`.
        # Reduce sender balance and increase receiver balance.
        if self.balance >= amount:
            self.balance -= amount
            reciver_account.balance += amount
            print(f"₹{amount} transferred from {self.account_holder} to {reciver_account.account_holder}")
        else:
            print(f"❌ Transfer Failed! Insufficient funds in {self.account_holder}'s account")
    def show_balance(self):
        print(f"🏦 {self.account_holder} bank Balance: ₹{self.balance}")
account1=bankaccount("Kiran",20000)
account2=bankaccount("Karthik",0)
account1.send_money(account2,500)
account1.send_money(account2,3000)
account1.show_balance()