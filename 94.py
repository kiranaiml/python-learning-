# THE NEOBANK ENGINE
class masteraccount:
    def __init__(self,account_holder,):
        self.account_holder=account_holder
        self._balance=0
    def get_balance(self):
        return self._balance
    def deposit(self,amount):
        self.amount=amount
        if amount<0:
            print("Invaild depposit amount")
        else:
            amount+=self._balance
            print(f"Deposit amount:₹{amount} ")
    def spend(self,amount):
        if amount>self._balance:
            print("Insufficient funds!")
        else:
            self._balance-=amount
            print(f"Spend:{amount}")
    def process_payment(self,amount=None):
        if amount==None:
            self.spend(100)
        else:
            self.spend(amount)
class creditcard(masteraccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.__creditcard = 50000
    def spend(self, amount):
        if (self._balance - amount) < -self.__creditcard:
            print("❌card dicline ! due excede ₹50000 limit")
        else:
            self._balance -= amount
            print(f"✅ Credit card charged: ₹{amount}")
checking=masteraccount("Kiran")
visa=creditcard("Kiran")
checking.deposit(3300)
checking.process_payment()
checking.deposit(20000)
checking.process_payment()
visa.deposit(2000)
visa.spend(400)
visa.spend(1000)