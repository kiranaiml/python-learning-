# THE GLOBAL FREIGHT LOGISTICS ENGINE

class Crate:
    def __init__(self, content_name, quantity, weight_per_unit):
        self.content_name = content_name
        self.quantity = quantity
        self.weight_per_unit = weight_per_unit
    def get_total_weight(self):
        return self.quantity * self.weight_per_unit

    def __str__(self):
        return f"[CRATE] {self.content_name} | Qty: {self.quantity} | Weight: {self.get_total_weight()}kg"

    def __add__(self, other_crate):
        if self.content_name == other_crate.content_name:
            return Crate(self.content_name, self.quantity + other_crate.quantity, self.weight_per_unit)
        else:
            print("❌ Error: Cannot merge crates of different contents!")
            return None

class CargoShip:
    def __init__(self, ship_name, max_weight_capacity):
        self.ship_name = ship_name
        self.max_weight_capacity = max_weight_capacity
        self.manifest = []

    def load_cargo(self, new_crate):
        current_total_weight = 0
        for crate in self.manifest:
            current_total_weight += crate.get_total_weight()
        if current_total_weight + new_crate.get_total_weight() > self.max_weight_capacity:
            print(f"⛔ OVERLOAD ALERT! {self.ship_name} cannot hold the {new_crate.content_name} crate.")
        else:
            self.manifest.append(new_crate)
            print(f"✅ Loaded {new_crate.content_name} onto {self.ship_name}.")

    def inspect_ship(self):
        print(f"🚢 --- {self.ship_name} Manifest ---")
        for crate in self.manifest:
            print(crate)


if __name__ == "__main__":
    my_ship = CargoShip("Maersk Alpha", 5000) 
    crate1 = Crate("Medical Supplies", 100, 5)   
    crate2 = Crate("Medical Supplies", 50, 5)    
    crate3 = Crate("Car Engines", 10, 300)       
    crate4 = Crate("Steel Beams", 20, 100)      
    print("--- Merging Crates ---")
    merged_medical_crate = crate1 + crate2 
    invalid_merge = crate1 + crate3 
    print("\n--- Loading Phase ---")
    my_ship.load_cargo(merged_medical_crate) 
    my_ship.load_cargo(crate3)        
    my_ship.load_cargo(crate4)               
    print("\n")
    my_ship.inspect_ship()