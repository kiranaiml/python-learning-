from abc import ABC,abstractmethod
class coffeereceipt(ABC):
    @abstractmethod
    def asking(self):
        pass
class bru(coffeereceipt):
    def asking(self):
        print("Coffe is ready wait 5 minute")
class strongbru(coffeereceipt):
    def asking(self):
        print("Your Strong coffee id ready our staff serve you")
class ordersystem :
    def proccessing(self,receipt):
        print("Proccessing your coffee...")
        receipt.asking()