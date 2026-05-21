#THE VEHICLE REGISTRATION ENGINE
class vechile:
    def __init__(self,brand,model ,car_type="sedan"):
        self.brand=brand
        self.model=model
        self.car_type=car_type
    def show_details(self):
        print(f"Vechile Registered: {self.brand} {self.model} | Type:{self.car_type}")
car=vechile("Toyoto","Camry")
car1=vechile("Mahindra","Thar","SUV")
car.show_details()
car1.show_details()