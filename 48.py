#Dictionaries learning
#challenge name="The Tech-Store Inventory"
inventory={
    "laptop":50000,
    "Mouse":500,
    "keyboard":1500
}
new_product=input("Enter the name of a new product:")
new_price=int(input("Enter the price for this product:"))
inventory[new_product]=new_price
inventory["Mouse"]+=150
print("\n"+"="*40)
print("\n___The Tech-Store Inventory___")
print("\n"+"="*40)
print(f"\nThe price of the Keyboard is: ₹{inventory['keyboard']}")
print(f"Final Updated Inventory: {inventory}")
print("\n"+"="*40)
print("\n        THANK YOU FOR VISITING     ")
print("\n"+"="*40)
