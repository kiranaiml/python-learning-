#"Smart Health Insurance Calculator"
user_name=str(input("Name:  "))
age=int(input("Age:  "))
if age<18:
    print("SORRY!,we only provide insurance for adults.")
else:
    q1=input("Do you smoke?(Yes/no:  )").lower()
    q2=input("Do you exercise?(Yes/no):  ").lower()
    q3=input("choice: 'Basic' or 'Premium':  ").lower()
 
if q3=="basic":
   price=200#pricing
else:
    price=500

if q1=="yes":#Athlete Discount
   price+=100#smoking tax added$100
else:
 price-=50#exercise discount$50
 total=price
 service_fee=0.05
 fee=round(total*service_fee,2) 
 final_total=total+fee
 user_id =user_name[0::2].upper()+str(age)[0:1]
#the recipt
print("\n"+"-"*30)
print("\n____Smart Health Insurance____")
print("\n"+"-"*30)
print(f"User id: {user_id}")
print(f"Name: {user_name}")
print(f"Package type: {price}")
print(f"Habit: {q1}")
print(f"Smoker: {q1}")
print(f"Exercise: {q2}")
print(f"Total: {total}")
print(f"Service fee: {service_fee}")
print(f"Final Total: {final_total}")
print("\n"+"-"*30)
print("\nTHANKS FOR VISTING US!")
print("\n"+"-"*30)