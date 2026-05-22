#THE HIGHWAY RIDER ENGINE
class motercycle:
    def __init__(self,rider_name):
        self.rider_name=rider_name
        self.rider_name=rider_name
        self._kilometer_ridden=0
    def check_ododmeter(self):
        print(f"🏍️ {self.rider_name} has ridden {self._kilometer_ridden} km.")
    def ride(self,km):
        if km==0:
            print("Invaild distance")
        else:
            km+=self._kilometer_ridden
            print(f"✅rode{km} kilometer")
    def pit_stop(self,location=None):
        if location==None:
            print("🛑 Stopped for a water break on the side of the road.")
        else:
            print(f"🛑 Stopped to explore the waterfalls at {location}!")
class offroad(motercycle):
    def ride(self, km):
        km*=self._kilometer_ridden
        print(f"🌲 Off-road mode! Rode {km} km, but it counts as {km * 2} km of engine wear!")
if __name__ == "__main__":
    print("--- Standard Bike Tests ---")
    bike1 = motercycle("Kiran")
    bike1.ride(-50)             
    bike1.ride(100)             
    bike1.pit_stop()       
    bike1.pit_stop("Sakleshpura") 
    bike1.check_ododmeter()       

    print("\n--- Off-Road Bike Tests ---")
    bike2 = offroad("Karthik""&""kushal")
    bike2.ride(50)               
    bike2.check_ododmeter()       