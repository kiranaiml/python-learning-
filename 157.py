while True:
    print("Welcome to the  SBI ATM")
    print("1: Balance | 2: Withdraw | 3: Deposit")

    user_choice = input("Please select an option: ")
    match user_choice:
        case "1":
            print("Checking balance")
        case "2": 
            
            print("How much you like to withdraw?")
        case "3":
            print("Please insert your deposit amount")
        case _,if user_choice >3:
            print("ERROR: Invaild selceltion")

