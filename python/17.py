#"Winter Jacket Discount Store"
name=str(input("Name: "))
num_of_jackets=int(input("How many jackets:  "))
subtotal=int( num_of_jackets*100)
if num_of_jackets >= 3:
    discount=0.20
elif num_of_jackets == 2:
    discount=0.10
else:
    discount=0
discount_amount= discount*subtotal
final_total=round(subtotal-discount_amount,2)
print("\n____store receipt____")
print(f"Hey! {name}")
print(f"MRP bill: {subtotal}")
print(f"Store discount:{discount_amount}")
print(f"final bill:{final_total} only-")