
#space colony cargo ship
ship_name = input("Ship name: ")
cargo_weight = int(input("Total Cargo Weight (Tons): ")) 
fuel_price = float(input("Price of fuel per liter: "))
total_fuel_needed = cargo_weight * 125
total_cost = round(total_fuel_needed * fuel_price, 2)
full_containers = cargo_weight // 12
leftover_tons = cargo_weight % 12
code_letters = ship_name[0:3].upper()
security_code = code_letters + str(full_containers)
print(f"\n--- MISSION MANIFEST: {security_code} ---")
print(f"Ship: {ship_name}")
print(f"Containers Needed: {full_containers} containers and {leftover_tons} extra tons.")
print(f"Total Fuel Cost: ${total_cost}")
