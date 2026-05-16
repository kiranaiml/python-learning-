#The Arcade Score Logger
master_list=[]
while True:
    score=input("Enter your game score: ")
    if score=="101" or score=="999":
        print("Invalid entry.Score discaded.")
        continue
    elif score=="close":
        print("Arcade closing. Saving data....")
        break
    else:
        master_list.append(score)
print(f"\nFinal list is: {master_list}")