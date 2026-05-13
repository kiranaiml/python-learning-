#"The Luxury Car Rental System" 
car_choice=str(input("car choice(Sedan/SUV): ")).lower()
price=int(input("price for car:'Sedan($50/day)or SUV($80/day)."))
days=int(input("How many days are they renting? "))
age=int(input("How old is the driver?"))
insurance=(input("Do they want'Full coverage'?(yes/no)"))
if age<21:
    print("Sorry, you must be 21 to rent a vechicle.")
else:
    if car_choice=='sedan':
        price_per_day=50
    else:
        price_per_day=80
        rental_subtotal=price*days
        final_total=rental_subtotal
if age>=21 and age<= 25:
    final_total+=20
    print(">> Young Driver Surcharge added: +$20")
if days>7:
    print(">> Loyalty Discount applied: -$30")
    final_total-=30
if insurance=='yes':
    insurance_cost=15*days
    final_total+=insurance_cost
    print(f">> Insurance added: +${insurance_cost}")
    booking_id=car_choice[0:1]+str(age)[-1]
    print("\n" + "="*35)
    print("   THE LUXURY CAR RENTAL RECEIPT")
    print("="*35)
    print(f"Booking ID:   {booking_id}")
    print(f"Car Choice:   {car_choice.capitalize()}")
    print(f"Days:         {days}")
    print(f"Subtotal:     ${rental_subtotal}")
    print("-" * 35)
    print(f"FINAL TOTAL:  ${final_total}")
    print("="*35)