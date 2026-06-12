class MilkReceipt:
    def __init__(self, code):
        self.code = code

    def calculate_rate(self, fat, snf):
        if fat >= 4.0 and snf >= 8.5:
            return 6.50
        if fat >= 3.5 and snf >= 8.0:
            return 6.00
        if fat >= 3.0 and snf >= 7.5:
            return 5.50
        return 5.00

    def calculate_amount(self, fat, snf, quantity):
        self.fat = fat
        self.snf = snf
        self.quantity = quantity
        self.rate = self.calculate_rate(fat, snf)
        self.amount = self.rate * quantity
        return self.amount

    def print_receipt(self, fat, snf, quantity):
        total = self.calculate_amount(fat, snf, quantity)
        print("\n===== Dairy Milk Receipt =====")
        print(f"Milk Code        : {self.code}")
        print(f"Fat Percentage   : {self.fat:.2f}%")
        print(f"SNF Percentage   : {self.snf:.2f}%")
        print(f"Quantity (Ltrs)  : {self.quantity:.2f}")
        print(f"Rate per Litre   : ₹{self.rate:.2f}")
        print(f"Total Amount     : ₹{total:.2f}")
        print("==============================\n")


def main():
    code = input("Enter your milk code: ").strip()
    try:
        fat = float(input("Enter fat percentage: "))
        snf = float(input("Enter SNF percentage: "))
        quantity = float(input("Enter total milk quantity (litres): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for fat, SNF, and quantity.")
        return

    receipt = MilkReceipt(code)
    receipt.print_receipt(fat, snf, quantity)


if __name__ == "__main__":
    main()