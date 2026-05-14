#"The Hassan Agri-Export Manager"
warehouse_info=("WH-45","Hassan",5000)
current_stock=[1200,450,900,1500]
current_stock.append(800)
current_stock.remove(450)
total_weight=sum(current_stock)
set_alpa={"Farmer_Ali", "Farmer_Suresh", "Farmer_Meena"}
set_beta = {"Farmer_Meena", "Farmer_Rahul", "Farmer_Kiran"}
master_farmers=(set_alpa.union(set_beta))
common_framers=(set_alpa & set_beta)
space_left=5000-total_weight
if total_weight>5000:
    status_massage=(f"OVERLOAD! Remove {space_left} kg immediately.")
elif space_left<500:
    status_massage=(f"Warning: Warehouse almost full.")
else:
    status_massage=(f"Safe: You can still fit {space_left}  kg.")
    print("\n"+"="*50)
    print('\n___The Hassan Agri-Export Manager___')
    print("\n"+"="*50)
    print("\nWarehouse:[Hassan](WH-45)")
    print(f"Current stock list:{current_stock}")
    print(f"Unique Farmers Count:{master_farmers}")
    print(f"Common farmer:{common_framers}")
    print(f"Status:{status_massage}")
    print("\n"+"="*50)
    print("\n   THANK YOU    ")
    print("\n"+"="*50)