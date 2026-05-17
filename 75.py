#The Highway Fuel Tracker
total_trip_cost=0
def add_fuel_stop(location,liters,price_per_liter):
    global total_trip_cost
    stop_cost=liters*price_per_liter
    total_trip_cost+=stop_cost
    print(f"Refueled at {location} | {liters}L added | Paid:₹{stop_cost}")
    
add_fuel_stop(location="Hassan",liters=5,price_per_liter=106)
add_fuel_stop(location="Sakleshpura",liters=3,price_per_liter=106)
print(f"\ntotal Fuel Expenses: ₹{total_trip_cost}")