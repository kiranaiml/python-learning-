#learning while looping and break and continue and nested loop
# the project name="The Infinite Security Scanner"

while True:
    ip = input("Enter IP to scan: ")
    
    if ip == "ignore":
        print("Skipping...")
        continue 

    elif ip == "admin":
        print("System shutting down.")
        break 
    else: 
        print("Target locked. Commencing scan...")
        
    
        for i in range(3):
            print("Scanning port...")