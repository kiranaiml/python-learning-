#The Smart Parking Garage
open_spots=0
parking_lot = [
    ["Car", "Empty", "Car"],
    ["Empty", "Empty", "Car"],
    ["Car", "Car", "Car"] 
]
for level_index,level_data in enumerate(parking_lot):
    for spot_index,spot_status in enumerate(level_data):
        if spot_status=="Empty":
            open_spots+=1
            print(f"Level {level_index}, Spot {spot_index} is open.")
print(f"\nScan completed.Total open spots: {open_spots}")