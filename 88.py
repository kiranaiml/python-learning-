#THE WATERFALL ROAD TRIP TRACKER
class roadtrip:
    def __init__(self,destination,km_ridden=0):
        self.destination=destination
        self.km_ridden=km_ridden
    def ride(self,distance):
        self.km_ridden += distance
        print(f"[UPDATE] rode {distance} km towdas {self.destination}")
    def check_odometer(self):
        print(f"-----Trip to {self.destination} | Total Distance convert: {self.km_ridden} km-----")
my_trip=roadtrip("Forest Waterfalls")
my_trip.check_odometer()
my_trip.ride(45)
my_trip.ride(30)
my_trip.check_odometer()