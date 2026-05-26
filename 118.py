
class Vehicle:
    def move(self):
        pass

class MotorizedVehicle(Vehicle):
    def start_engine(self):
        print("Engine roaring! Ready for the trails.")
        
    def move(self):
        self.start_engine()

class ManualVehicle(Vehicle):
    def pedal(self):
        print("Pedaling hard up the mountain!")
        
    def move(self):
        self.pedal()

def start_trip(vehicle_object):
    vehicle_object.move()

my_moto = MotorizedVehicle()
my_bike = ManualVehicle()

print("--- Starting Moto Trip ---")
start_trip(my_moto) 

print("\n--- Starting Bike Trip ---")
start_trip(my_bike)
