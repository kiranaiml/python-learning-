# 1. THE BLUEPRINT (Just holds the data structure)
class Coffee:
    def __init__(self, name_of_coffee):
        self.name_of_coffee = name_of_coffee
menu = []
while True:
    print("\n*** Hey 👋 Welcome to our shop ***")
    print("1. Order coffee | 2. View your menu | 3. Exit")
    
    user_input = input("Enter your choice: ")
    
    match user_input:
        case "1":
            type_coffee = input("What type of coffee do you want?: ")
            new_order = Coffee(type_coffee) 
            menu.append(new_order.name_of_coffee) 
            print("Wait 5 minutes, your coffee ☕️ is ready!")
            
        case "2":
            print(f"Your menu: {menu}")
            
        case "3":
            print("Have a nice day! Bye👋")
            break
            
        case _:
            print("Invalid choice, please select 1, 2, or 3.")
                 