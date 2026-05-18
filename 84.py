#The Zero-Death K/D Calculator 
def calculate_kd(kills, deaths):
    try:
        ratio = kills/deaths
        print(f"Player K/D: {ratio}")
    except ZeroDivisionError:
            print("Error: Cannot divide by Zero!Player is invincible")
calculate_kd(10,2)
calculate_kd(15,0)