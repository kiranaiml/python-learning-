# The E-Commerce Checkout Engine
class product:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def calculate_final_price(self):
        return self.base_price


class physicalitem(product):
    def __init__(self, name, base_price, weight_in_kg):
        super().__init__(name, base_price)
        self.weight_in_kg = weight_in_kg

    def calculate_final_price(self):
        return self.base_price + (self.weight_in_kg * 50)


class digitalitem(product):
    def __init__(self, name, base_price):
        super().__init__(name, base_price)

    def calculate_final_price(self):
        return self.base_price + 20


class shoppingcart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart_item = []

    def add_product(self, product):
        self.cart_item.append(product)
        print(f"✅ Added {product.name} to the cart.")

    def checkout(self):
        grand_total = 0
        print("🧾 ---Checkout Receipt---")
        for item in self.cart_item:
            price = item.calculate_final_price()
            grand_total += price
            print(f"{item.name} : ₹{price}")

        print(f"💳 Total Amount Due: ₹{grand_total}")
if __name__ == "__main__":
    my_cart = shoppingcart("Kiran")
    item1 = physicalitem("Gaming Laptop", 80000, 3)  # 3kg heavy!
    item2 = digitalitem("Python Course Pro", 1500)
    item3 = physicalitem("Wireless Mouse", 1000, 0.5) # Half a kilo
    my_cart.add_product(item1)
    my_cart.add_product(item2)
    my_cart.add_product(item3)
    print("\n")
    my_cart.checkout()