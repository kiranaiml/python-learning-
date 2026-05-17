#The Garage Inventory
garage_inventory={
    "Helmets": 2,
    "Riding Jackets": 1,
    "Gloves": 3
}
garage_inventory["boots"]=1
for item, quantity in garage_inventory.items():
    print(f"-{item}: {quantity} Pairs")
