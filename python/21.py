# --- PREMIUM ADVENTURE TRAVEL AGENCY ---
print("=== Welcome to the Premium Travel Booking System ===")
name = input("Enter Customer Name: ")
age = int(input("Enter Customer Age: "))
if age < 18:
    print(f"Sorry {name}, you must be 18 or older to book a trip.")
else:
    print(f"\nHello {name}, let's plan your adventure!")
    
    destination = input("Choose destination (Beach / Mountain / City): ").lower()
    people = int(input("How many people are traveling? "))
    if destination == "beach":
        price_per_person = 500
    elif destination == "mountain":
        price_per_person = 700
    else:
        price_per_person = 400 
    subtotal = price_per_person * people
    discount = 0
    if people > 5:
        discount = 100
        print(">> Group Discount Applied: -$100")
    final_bill = subtotal - discount
    print("\n" + "="*30)
    print("      TRAVEL RECEIPT")
    print("="*30)
    print(f"Customer:    {name}")
    print(f"Destination: {destination.capitalize()}")
    print(f"Group Size:  {people} people")
    print(f"Subtotal:    ${subtotal}")
    print(f"Discount:    -${discount}")
    print("-" * 30)
    print(f"FINAL TOTAL: ${final_bill}")
    print("="*30)
    print("Thank you for booking with us!")