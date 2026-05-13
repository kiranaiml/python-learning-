#"Smart Tech Store"
product=str(input("(phone,laptop or tablet: )"))
quantity=int(input("quantity:  "))
student=(input("student(yes/no):  "))
if product=="laptop":
   price_for_product=1000
elif product=="phone":
    price_for_product=500
else:
    price_for_product=300
subtotal=price_for_product*quantity
discount_amount=0
if quantity>3:
    discount_amount=0.10
    print(" you got 10%_discount")
student_discount=0
if student=="yes":
    student_discount=50
    print("HURRy! you got $50 off")
total_after_discount=subtotal-discount_amount-student_discount

tax=total_after_discount*0.08

final_total=total_after_discount+tax

print("\n"+"="*30 )
print("\n____TECH STORE RECEIPT____")
print("\n"+"="*30 )
print(f"Item:        {product}")
print(f"subtotal:     {subtotal}")
print(f"discounts:     {total_after_discount}")
print(f"tax(8%):     {round(tax)}")
print(f"final total:     {round(final_total)}")
print("\n"+"="*30 )
print("\n THANKS FOR VIST OUR STORE")

