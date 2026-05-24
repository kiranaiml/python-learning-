from abc import ABC, abstractmethod

class SpeedTrackable(ABC):
    @abstractmethod
    def show_speed(self):
        pass
class ClimateControllable(ABC):
    @abstractmethod
    def turn_on_ac(self): 
        pass
class LuxuryCar(SpeedTrackable, ClimateControllable):
    def show_speed(self):
        print("🚗 Displaying speed on the digital dash.")
        
    def turn_on_ac(self):
        print("❄️ Blowing cold air into the cabin.")
class Motorcycle(SpeedTrackable): 
    def show_speed(self):
        print("🏍️ Displaying speed on the analog dial.")
if __name__ == "__main__":
    my_car = LuxuryCar()
    my_bike = Motorcycle()
    
    print("--- Testing the Car ---")
    my_car.show_speed()
    my_car.turn_on_ac()
    
    print("\n--- Testing the Motorcycle ---")
    my_bike.show_speed()