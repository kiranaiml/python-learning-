#"The AI Airport Security & Immigration Hub"
name = input("Passenger Name: ")
country = input("Passport Country (USA/India/UK): ").lower()
ticket_class = input("Ticket Class (Economy/Business/First): ").lower()
weight = int(input("Luggage Weight (kg): "))
risk = int(input("Security Risk Level (1-10): "))

# 1. THE GATEKEEPER
if risk >= 8:
    print("\n" + "!"*50)
    print("SECURITY ALERT: PASSENGER DETAINED FOR INTERROGATION.")
    print("!"*50)
else:
    # 2. VISA LOGIC
    if country == "usa" or country == "uk":
        visa = "Approved"
    elif country == "india":
        if ticket_class == "business" or ticket_class == "first":
            visa = "Approved"
        else:
            visa = "Pending Manual Check"
    else:
        visa = "Check Required"

    # 3. LUGGAGE LOGIC
    if ticket_class == "economy":
        limit = 20
        base_price = 500
    else: # Business or First
        limit = 40
        base_price = 1200 if ticket_class == "business" else 3000

    # Calculate Penalty (Only if over limit)
    penalty = 0
    if weight > limit:
        penalty = (weight - limit) * 15
    
    # 4. PRIORITY LOGIC
    if ticket_class == "first" and risk < 3:
        priority = "VIP-FAST"
    else:
        priority = "STANDARD"

    # 5. DATA GENERATION
    pass_id = country[0].upper() + name[-3:].upper() + ticket_class[0].upper()
    total_bill = base_price + penalty

    # 6. THE BOARDING PASS DASHBOARD
    print("\n" + "="*55)
    print("      AI AIRPORT IMMIGRATION HUB - BOARDING PASS")
    print("="*55)
    print(f"BOARDING PASS ID:    {pass_id}")
    print(f"PASSENGER NAME:      {name.title()}")
    print(f"VISA STATUS:         {visa}")
    print(f"BOARDING PRIORITY:   {priority}")
    print("-" * 55)
    print(f"LUGGAGE OVERAGE FEE: ${penalty}")
    print(f"FINAL TICKET COST:   ${total_bill}")
    print("="*55)
    print("         SAFE FLIGHTS & CLEAR SKIES!")
    print("="*55)