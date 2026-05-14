#The Karnataka Road Trip Planner"
trip=("Hassan","Mysuru",120)
liters_needed=120/15
fuel_price=100
food=1200
total_cost=(liters_needed*fuel_price)+food
bag=["Phone","Clothes","Wallet"]
bag.append("camera")
bag.remove("camera")
bag.append("Snacks")
bag.sort()
my_sites={"palace","Zoo","KRS Dam","Temple"}
friend_sites={"Palace","Lalitha","KRS Dam"}
common=my_sites & friend_sites
unique=my_sites.union(friend_sites)
if total_cost<2000:
    print("Status: Expensive Trip. Need more cash!")
else:
    print("Status: Budget Friendly. Let's go!")
    print("\n"+"="*50)
    print("\n__The Karnataka Road Trip Planner__")
    print("\n"+"="*45)
    print("\nRoute:[Hassan] to [Mysuru]")
    print(f"Liters needed: {liters_needed}")
    print(f"Final bag: {bag}")
    print(f"Common sites: {common}")
    print(f"total unique stops:{unique}")
    print("\n"+"="*50)
    print("\n       ***THANK YOU***       ")
    print("\n"+"="*50)