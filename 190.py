#Build a BankAccount class where a 'Savings' account object (starting with 5000) uses a method to transfer 1500 directly into a completely separate 'Checking' account object (starting with 1000). Print both final balances.

class bankaccount:  
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
    def transfer(self,transfer_amount):
        if transfer_amount>=100000:
            print(f"Transfer amount of {transfer_amount} is. Hit daily limit, Transcation failed")
        elif self.balance<transfer_amount:
            print(f"Insufficient Payment")
        else:
            self.balance-=transfer_amount
            print(f"Your Transcartion amount {transfer_amount} is successfully transfered. ")
    def check_balance(self):
        print(f"Account holder:{self.account_holder}\nBalance : {self.balance}")
my_bank=bankaccount("kiran",6000)
my_bank.transfer(10000)
my_bank.check_balance()