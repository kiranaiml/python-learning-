#fire free store engine
class playeraccount:
    def __init__(self,username,diamonds=500):
        self.diamonds=diamonds
        self.username=username
    def buy_item(self,item_name,cost):
        self.item_name=item_name
        self.cost=cost
        if self.diamonds>=cost:
            self.diamonds-=cost
            print(f"{self.username} successfully bought {item_name}! Remaining diamonds: {self.diamonds}")
        else:
            print(f"❎Transcation Failed! {self.username} needs {cost} diamonds to buy {item_name}")
    def check_balance(self):
        print(f"----{self.username}'s Wallet: {self.diamonds} Daimonds----")
gamer=playeraccount("karthik",800)
gamer.check_balance()
gamer.buy_item("MP40 Cobra Skin",600)
gamer.buy_item("Elite Pass",400)
gamer.check_balance()
