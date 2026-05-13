#"Rollercoaster Gate"
name=str(input("name: "))
person_age=int(input("age: "))
height=float(input("height of person in inches: "))
if person_age >= 10 and height>=48:
    print("WELCOME aboard! Enjoy the ride.")
elif person_age >= 10:
    print("you are old enoung,but too short for this ride")
elif height >= 48:
    print("you are age not meet our recuirement, but you are height perfect. ")
else:
    print("Sorry,you do not the reqirements yet.")