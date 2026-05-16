#The E-Commerce Cart Manager
cart=[]
while True:
    item=input("Enter an item to buy (or type 'checkout' to pay):")
    if item=="checkout":
        print("proceeding to payment gateway....")
        break
    elif item=="sold out":
        print("sorry,this item is unavailable.Skipping...")
        continue
    else:
        cart.append(item)
        print("Item added to cart.")
print(f'\nFinal Shopping Cart.')
