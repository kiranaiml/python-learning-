#THE VEHICLE RENTAL SHOP
class rentalshop:
    def __init__(self,shop_name):
        self.__total_revenue=0
        self.shop_name=shop_name
    def receive_payment(self,amount):
        self.__total_revenue+=amount
    def show_revenue(self):
        print(f"🏦{self.shop_name} Total Revenue : ₹{self.__total_revenue}")
class rentalvehicle:
    def __init__(self, brand, days_rented):
        self.brand = brand
        self.days_rented = days_rented
class motorcycle(rentalvehicle):
    def __init__(self,brand,days_rented):
        super().__init__(brand, days_rented)
    def calculate_rent(self):
        # Motorcycle rate: ₹500 per day
        return self.days_rented * 500
class car(rentalvehicle):
    def __init__(self,brand,days_rented,):
        super().__init__(brand,days_rented)
    def calculate_rent(self):
        return self.days_rented*1500
my_shop=rentalshop("Kiran's Rental")
bike_rental=motorcycle("Royal Enfield",30)
car_rental=car("Mahindra Thar",2)
my_shop.receive_payment(bike_rental.calculate_rent())
my_shop.receive_payment(car_rental.calculate_rent())
my_shop.show_revenue()