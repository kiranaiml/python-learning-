#"The International Shipping Hub"
name=input("Name: ")
weight= float(input("WEIGHT IN KILOGRAM: "))
destination=input("DESTINATION(USA,UK OR OTHER): ").lower()
speed=("SPEED:  ")
if weight>50:
    print("package too heavy for standard delivery.Must use freight shipping.")
    price=0
if destination=='usa':
    price=20
elif destination=='uk':
    price=30
else:
    price=50
if weight>10:
    price+=15
    print("heavy weight")
if speed=='express':
    price*=1.5
    print("express shipping applied 50%_increase")
    tracking_id = destination[0].upper() + str (weight).replace(".", "")
print("\n"+"="*30)
print("\n___INTERNATIONAL SHIPPING____")
print("\n"+"="*30)
print(f"\n TRACKING ID: {tracking_id}")
print(f"\n NAME       : {name}")
print(f"\n DESTINATION: {destination}")
print(f"\n SHIPPING COST:{round(price,2)}")
print("\n"+"="*30)
print("!!THANKS FOR VISTING US!!")
print("\n"+"="*30)