name=input("costomer's name:  ")
total_unit=float(input("montly kwh used: "))
usage_cost=total_unit*0.12
sub_total=round(usage_cost+15.000)
tax_amount=round(sub_total*0.05)
total_bill=sub_total+tax_amount
print(f"HELLo {name}! your total electricity bill for this month is ${total_bill}")