#learning SOLID principle of oop
class Invoice:
    def __init__(self, customer_name, total_amount):
        self.customer_name = customer_name
        self.total_amount = total_amount
class TaxCalculator:
    def calculate_tax(self, invoice):
        return invoice.total_amount * 0.08
class ReceiptPrinter:
    def print_receipt(self, invoice):
        print(f"--- RECEIPT ---")
        print(f"Customer: {invoice.customer_name}")
        print(f"Total: ₹{invoice.total_amount}")
        print(f"---------------")
class DatabaseSaver:
    def save_customer_data(self, invoice):
        print(f"Connecting to server... Saving {invoice.customer_name}'s invoice to SQL database.")

if __name__ == "__main__":
    my_invoice = Invoice("Kiran", 5000)
    calculator = TaxCalculator()
    printer = ReceiptPrinter()
    db_saver = DatabaseSaver()
    tax = calculator.calculate_tax(my_invoice)
    printer.print_receipt(my_invoice)
    db_saver.save_customer_data(my_invoice)