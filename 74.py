#The Sneaker Store Checkout
total_revenue=0

def sell_sneakers(shoe_name,price):
    global total_revenue
    total_revenue+=price
    tax_collected=price*0.18
    print(f"Sold:{shoe_name}|Price:₹{price}|Tax Collected:₹{tax_collected}")
sell_sneakers(shoe_name="Nike Air Forece1",price=7500)
sell_sneakers(shoe_name="PumaRS-X",price=4200)
print(F"\nTOTAL STORE REVENUE: ₹{total_revenue}")