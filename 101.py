from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    def process_transaction(self, amount):
        pass

class TransactionLimitError(Exception):
    pass
class UpiProvider(PaymentProvider):
    def __init__(self, upi_id):
        self.upi_id = upi_id
        
    def process_transaction(self, amount):
        if amount > 50000:
            raise TransactionLimitError("❌ UPI LIMIT EXCEEDED! MAXIMUM IS ₹50000")
        else:
            print(f"✅ Processing ₹{amount} via UPI to {self.upi_id}.")

class CreditCardProvider(PaymentProvider):
    def __init__(self, card_number):
        self.card_number = card_number
        
    def process_transaction(self, amount):
        final_amount = amount * 1.02 
        if final_amount > 200000:
            raise TransactionLimitError("❌ Credit card limit exceeded!")
        else:
            print(f"✅ Processing ₹{final_amount} (including 2% fee) via Card {self.card_number}.")

class PaymentRouter:
    def execute_payment(self, provider, amount):
        try:
            provider.process_transaction(amount)
        except TransactionLimitError as e:
            
            print(e)


# --- 🎬 The Execution Block ---
if __name__ == "__main__":
    # 1. Initialize the Router
    router = PaymentRouter()
    
    # 2. Initialize the Payment Methods
    my_upi = UpiProvider("kiran@okhdfc")
    my_card = CreditCardProvider("4111-2222-3333-4444")
    
    print("--- Standard Transactions ---")
    router.execute_payment(my_upi, 15000) 
    router.execute_payment(my_card, 100000) 
    
    print("\n--- High-Value Transactions (Testing Exceptions) ---")
    router.execute_payment(my_upi, 80000)
    router.execute_payment(my_card, 198000)