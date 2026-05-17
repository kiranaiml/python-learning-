# 1. THE GLOBAL VARIABLE (The Billboard)
#(learning function,gobal and local variables)
total_diamonds = 100 

def add_diamonds(bonus):
    global total_diamonds  
    
    total_diamonds+=bonus
    

    bonus = "Reward claimed!"
    
    print(bonus)
    print(f"Muruli now has {total_diamonds} diamonds.")

add_diamonds(bonus=50)