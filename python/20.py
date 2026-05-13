#"Smart Home Loan Calculator"
name=str(input("Name:  "))
sure_name=str(input("Sure Name: "))
age=int(input("Age:   "))
if age<21:
    print("Sorry! your are age not meet our recuirement. Try after '21'")
else:
    print("WELLCOME! ")
annual_income=int(input("what's your annual income:  "))
loan_amonut=float(input("loan amount: "))
credit_score=float(input("credit score:  "))
if credit_score<600:
    print("Loan denied: Credit score too low.")
if credit_score>=600  and (annual_income*4)>loan_amonut:
    print("Loan Approved with standard intrest rate.")
elif (annual_income*2)>=loan_amonut:
    print("loan approved with standard intrest rate.")
else:
    print("loan denied:income is too low for this loan amount.")
