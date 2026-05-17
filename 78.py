#The Motorcycle Trip Packer
def pack_for_trip(*gear,**route):
    for key, value in route.items():
        print(f"Route Info -> {key}: {value}")
        print("---Gear Packed---")
    for g in gear:
        print(f"- {g}")
pack_for_trip("Helmet", "Riding Jacket", "Gloves", "Boots", start="Bangalore", destination="Coorg", duration="3 days")