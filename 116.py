class RouteDatabase:
    def save(self, location):
        print(f"Saving {location} to the database...")

class FuelCalculator:
    def calculate(self, kilometers):
        print(f"Calculating cost for {kilometers}km...")

class PhotoEditor:
    def apply_filter(self, photo_name):
        print(f"Applying moody techno filter to {photo_name}...")


# --- THE MAIN SYSTEM (The Manager) ---

class MotoTripLogger:
    def __init__(self):
        self.db = RouteDatabase()
        self.fuel = FuelCalculator()
        self.editor = PhotoEditor()

    def run_full_log(self, location, distance, photo):
        print(f"--- Starting log for {location} ---")
        self.db.save(location)
        self.fuel.calculate(distance)
        self.editor.apply_filter(photo)
        print("--- Trip fully logged! ---")

# --- EXECUTION ---
my_weekend_ride = MotoTripLogger()
my_weekend_ride.run_full_log("Sakleshpura", 22, "waterfall_01.jpg")