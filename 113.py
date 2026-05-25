from abc import ABC, abstractmethod

# ❌ The "God" Blueprint (Violates ISP)
class making_coffee(ABC):
    @abstractmethod
    def brewer(self):
        pass
class payment_handle(ABC):
    @abstractmethod
    def chasier(self):
        pass

# ❌ The Broken Workers (Violates LSP because they crash the system!)
class Barista(making_coffee):
    def brewer(self):
        print("☕ Brewing a delicious espresso!")

    def chasier(self):
        # The Barista is yelling at us!
        print("Error: Baristas do not process payments.")

class Cashier(payment_handle):
    def brewer(self):
        # The Cashier is yelling at us!
        print("Error: Cashiers do not make coffee.")

    def chasier(self):
        print("💳 Processing customer payment.")
