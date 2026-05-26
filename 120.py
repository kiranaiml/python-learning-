from abc import ABC,abstractmethod
class ParagParikhFlexiCapAPI(ABC):
    @abstractmethod
    def __init__(self):
        # The manager builds its own low-level tool
        self.investment_broker = ParagParikhFlexiCapAPI()

class trip(ABC):
    @abstractmethod 
    def execute_end_of_day(self, location, content_type, device):
        # Task 1: Log the trip
        print(f"Saving {location} trip to the database...")
class process(ABC):
        def content_type (self):
            print( "Techno_Reel")
            print("Rendering 4K video with hip-hop beats...")
            pass 

            print("Sketch")
            print("Scanning architectural timber sketch...")
            return
class trade (ParagParikhFlexiCapAPI):
            def __init__(self):
                self.investment_broker.invest(500)
        
class data(trip):
        def execute_end_of_day(self, location, content_type, device):
           device.record_footage()
           device.upload_to_wifi()

# --- Execution ---
class GoPro:
    def record_footage(self):
        print("Recording trail ride...")
    def upload_to_wifi(self):
        raise Exception("Fatal Error: This GoPro model has no WiFi!")

# Running the day
my_system = ParagParikhFlexiCapAPI()
my_gopro = GoPro()

my_system.execute_end_of_day("Arsikere Waterfalls", "Techno_Reel", my_gopro)