from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, total_amount):
        pass
class RegularDiscount(DiscountStrategy):
    def calculate(self, total_amount):
        return total_amount # Full price

class VipDiscount(DiscountStrategy):
    def calculate(self, total_amount):
        return total_amount * 0.80 # 20% off

class StudentDiscount(DiscountStrategy):
    def calculate(self, total_amount):
        return total_amount * 0.90 # 10% off

class DiscountCalculator:
    def apply_discount(self, strategy, total_amount):
        return strategy.calculate(total_amount)
if __name__ == "__main__":
    calculator = DiscountCalculator()
    regular = RegularDiscount()
    vip = VipDiscount()
    student = StudentDiscount()
    
    cart_total = 100.00
    
    print(f"--- Calculating Checkout for ${cart_total} ---")
    reg_price = calculator.apply_discount(regular, cart_total)
    vip_price = calculator.apply_discount(vip, cart_total)
    student_price = calculator.apply_discount(student, cart_total)
    
    print(f"Regular Customer pays: ${reg_price:.2f}")
    print(f"VIP Customer pays: ${vip_price:.2f}")
    print(f"Student Customer pays: ${student_price:.2f}")