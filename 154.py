#The Offline Password Generator & Vault

while True:
    user_input=input("Enter a link (or type 'exit' to quit): ").lower()
    if user_input=="exit" or user_input=="break":
        print("The system is shotdown!!")
        break
    else:
        web_type=input("What website is this for: ")
        password=input("How many characters should the password be?: ")
        import random 
        import string
        all_characters = string.ascii_letters + string.digits + string.punctuation
        length = 12 
        new_password = ""
        for i in range(length):
            random_char = random.choice(all_characters)
            new_password = new_password + random_char

            print("Your new secure password is:")
            print(new_password)
        with open("password.txt", "a") as file:
            file.write(f"Website: {web_type} | Password: {new_password}\n")
            
        print("Success! Saved to password.txt")