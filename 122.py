from abc import ABC, abstractmethod

# --- 1. THE STRATEGY BLUEPRINT (Only One!) ---
# This is the single rule: Every strategy must have a 'calculate' method.
class RouteStrategy(ABC):
    @abstractmethod
    def calculate(self, start, destination):
        pass

# --- 2. THE SPECIFIC STRATEGIES (The Tools) ---
# These do the actual work. No 'if/elif' statements anywhere.

class FastestRoute(RouteStrategy):
    def calculate(self, start, destination):
        print(f"Routing {start} to {destination} via major highways. ETA: 2 hours.")

class ScenicRoute(RouteStrategy):
    def calculate(self, start, destination):
        print(f"Routing {start} to {destination} via forest trails. ETA: 4 hours.")

class FuelSaverRoute(RouteStrategy):
    def calculate(self, start, destination):
        print(f"Routing {start} to {destination} via flat roads. Lowest RPM limits.")


# --- 3. THE CONTEXT (The Navigator) ---

class GPSNavigator:
    def __init__(self, strategy: RouteStrategy):
        # We load a strategy in when we turn on the GPS
        self.strategy = strategy
        
    def set_strategy(self, new_strategy: RouteStrategy):
        # The secret weapon: Swapping the strategy on the fly!
        self.strategy = new_strategy

    def build_route(self, start, destination):
        # The GPS doesn't do any math. It just tells the strategy to run.
        self.strategy.calculate(start, destination)


# --- 4. EXECUTION ---

print("--- Morning Ride ---")
# Start the GPS with the Fastest strategy
my_gps = GPSNavigator(FastestRoute())
my_gps.build_route("Home", "Waterfalls")

print("\n--- Heading Back ---")
# We swap the tool on the fly! No if/elif statements. No rewriting code.
my_gps.set_strategy(ScenicRoute())
my_gps.build_route("Waterfalls", "Home")