#"The Mysuru Palace Ticket & Tour System"

palace_data = ("Mysuru Palace", 250.0, 5000)
leader_name = input("Group Leader's Name: ").title()
adults = int(input("Number of Adults: "))
children = int(input("Number of Children: "))
user = input("Is this a VIP group? (yes/no): ").lower()
members = []
members.append(input("Member 1: "))
members.append(input("Member 2: "))
canceled_person = input("Person who canceled: ")
if canceled_person in members:
    members.remove(canceled_person)
else:
    print(f"Notice: {canceled_person} is not in the list.")
general_areas = {"Main Hall", "Gardens", "Museum"}
vip_areas = {"Royal Armory", "Durbar Hall", "Museum"}
premium_areas = vip_areas.difference(general_areas) # VIP minus General
master_map = general_areas.union(vip_areas)
adult_total = adults * palace_data[1]   
children_total = children * (palace_data[1] / 2) 
subtotal = adult_total + children_total
total_people = adults + children
if user == "yes":
    subtotal = subtotal + (total_people * 100) 
    level = master_map
else:
    level = general_areas     
if subtotal > 1000:
    discount = subtotal * 0.10
    final_total = subtotal - discount
else:
    final_total = subtotal
print("\n" + "="*50)
print("___The Mysuru Palace Ticket & Tour System___")
print("="*50)
print(f"Palace Name: {palace_data[0]} | Daily Limit: {palace_data[2]}")
print(f"Group Leader: {leader_name}")
print(f"Final Guest List: {members}")
print(f"Headcount: {adults} Adults, {children} Children")
print(f"Allowed Access Zones: {level}")
print(f"Total Price to Pay: ₹{final_total}")
print("="*50)
print("                THANK YOU               ")
print("="*50)