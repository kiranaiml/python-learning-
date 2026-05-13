#"The Galactic Resort & Spa"
customer_name=str(input("CUSTOMER NAME:  "))
room_tier=str(input("standard($200/night),luxury($500/night),penthouse($1200/night):  "))
nights=int(input("How many nights are they staying?:  ")) 
guest_count=int(input("How many people are staying in the room? "))
membership=(input("Do you have 'GOLD'membership?(yes/no) ")).lower()
if guest_count<=0 and guest_count<0:
    print("Error: Invalid guest count.")
if guest_count>4:
    print("Sorry! max capacity is 4 guests per room.")
    room_cost=0
if room_tier=='standard':
    room_cost=200
elif room_tier=='luxury':
    room_cost=500
else:
    room_cost=1200
if guest_count==3 or 4:
    room_cost+=100
if nights>7:
    room_cost-=150
if membership=='yes':
    discount=0.20
    room_cost-=discount
    print("Gold Member Discount 20% OFF") 
    room_cost=1200
    subtotal=room_cost*nights 
    tax=(room_cost*0.12)
    total=round(tax+subtotal,2)
    user_id=customer_name[0:3].upper()+str(nights)[-1]+room_tier[0:5].upper()
    print("\n"+"="*30)
    print("\n---The Galactic Resort & Spa---")
    print("\n"+"="*30)
    print(f"User id: {user_id}")
    print(f"Room tier: {room_tier}")
    print(f"Subtotal(Before tax):  {subtotal}")
    print(f"Tax amount(12%): {tax}")
    print("\n"+"="*30)
    print(f"\nFinal total:{total}") 
    print("\n"+"="*30)                             