#"The Smart Toll & Traffic Manager"
vehicle_type=str(input("Vehicle type(car/truck/emergency): ")).lower()
time_of_day=int(input("Time of day: "))
weather=str(input("weather(clear/rain/snow): ")).lower()
plate_number=str(input("Plate Number: "))
e_pass=input("E-pass holder(yes/no): ").lower()
if vehicle_type=="emergency":
    price=0
    print("EMERGENCY VEHICLE DETECTED. OPENING GATE. FEE: $0")
    print("GATE STATUS: OPEN | FEE: $0")
    print("!"*30)
else:
    if vechicle_type=="car":
        price=5
    else:
        price=12
    
        if (7>=time_of_day<= 9) or (16>=time_of_day<= 19):
            price+=3
            print(">> Peak Hour Surcharge: +$3")
if weather=="snow" or weather=="rain":
    price+=2
    print(f">> Heavy {weather} Maintenance Fee: +$2")
else: 
    print("Road is clear enjoy your trip")
if e_pass=="yes":
    discount=price*0.15
    price-=discount
    print("You got E-PASS Discount 15%_off")
    transcation_id=plate_number[0:3]+str(time_of_day)[0:1]+weather[0:1]
    print("\n"+"="*50)
    print("\n__The Smart Toll & Traffic Manager Hassan")
    print("\n"+"="*50)
    print(f"TRANSACTION ID: {transcation_id}")
    print(f"VEHICLE TYPE: {vehicle_type}")
    print(f"PLATE NUMBER: {plate_number}")
    print(f"FINAL FEE:    {round(price,2)}")
    print("GATE TYPE:      OPEN")
    print("\n"+"-"*50)
    print("      HAVE A SAFE TRIP!")
    print("\n"+"-"*50)