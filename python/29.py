#"The Inventory Manager"
name=str(input("Name: "))
weight=int(input("Weight(in kg): "))
user=input("User is student(yes/no):  ").lower()
goal=str(input("lose or gain: ")).lower()
budget=(input("Basic($30) or Premium($80): ")).lower()
price=0
if  weight<40:
    print("Warning: Please consult a doctor before starting a gym plan.")
else: 
    if budget=='basic':
        price=30
    else:
        price=80
    if user=='yes':
        price=price*0.80
        print("you got student discount 20%")
    if goal=="lose":
        if weight>100:
            print("plan = 'High-intensity cardio and running'")
        else:
            print("plan = 'High-intensity cardio and running'")
    else:
        if weight<60:
            print("Plan = 'light weight and high-protien diet'")
        else:
            print("Plan = 'Heavy lifting and strength training'")

if  weight>100:
    print("Plan: Low-impact walking and swimming.")
else:
    print("Plan: High-intensity cardio and running.")
if  weight<60:
    print("Plan: Light weights and high-protein diet.")
else:
    print("Plan: Heavy lifting and strength training.")
    member_id=name[0:1].upper()+str(weight)[0:1]+goal[0:-2]
    print("\n"+"="*30)
    print("\n____The Smart Diet & Gym Assistant Recipt____")
    print("\n"+"="*30)
    print(f"NAME:  {name}")
    print(f"GOAL:  {goal.upper()}")
    print(f"PLAN:   {budget}")
    print(f"MEMBER ID: {member_id}")
   
    print("\n"+"-"*30)
    print(f"FINAL PRICE: {price}")
    print("\n"+"="*30)
    print("    STAY HEALTHY & STRONG!")