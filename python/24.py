#"The Smart Cinema Booking System"
name=str(input("customer name: "))
age=int(input("Age: "))
Movie_time=int(input("Movie Time: "))
combo=input("popcorn combo(yes/no): ").lower()
if age<=13:
    print(" Note: You are restricted to G-rated movies.")
else:
    print("Access granted to all movies.")
if age>=60:
    ticket=10 
else: 
    ticket=15
if Movie_time<16:
    ticket-=2
    print(" Matinee discount applied: -$2")
if combo=='yes':
    ticket+=8
    print(" popcorn combo added: +8")
else:
    ticket=15
    tax=0.07
    tax_amount=round(ticket*tax,2)
    final=tax_amount+ticket
    user_id=name[0:3].upper()+str(age)[-1]
print("\n"+"="*30)
print("^^^The Smart Cinema^^^")
print("="*30)
print(f"USER ID: {user_id}")
print(f"TOTAL: {ticket}")
print(f"TAX(7%): {tax_amount}")
print(f"FINAL TOTAL: {final}")
print("\n"+"="*30)
print("**THANKS FOR VISTING US!**")
print("\n"+"="*30)