user_name=  input('captain name: ')
total_distance=float (input ('the kilometer of trip: '))
number_of_ports=int (input("ship will vist:  "))


total_fuel_needed=total_distance*250
total_fuel_cost=total_distance*1.15
total_port_fee=round(number_of_ports*12500)
grant_total=round(total_fuel_cost+ total_port_fee)

print(f"hello {user_name} the total {total_fuel_needed} liters of fuel used,and the final {grant_total} total price")
