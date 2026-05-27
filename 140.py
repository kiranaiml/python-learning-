import json 

player_profile = {
    "username": "karthik",
    "rank": "Heroic",
    "kills": 1250
}

print("--- Initiating Server Save ---")

# 🚨 MISSION 1: Open "player_save.json" in "w" (Write) mode and dump the data!
with open("player_save.json", "w") as file:
    json.dump(player_profile, file)
    print("Profile successfully saved to hard drive!")

print("\n--- Simulating Server Restart ---\n")

# 🚨 MISSION 2: Open "player_save.json" in "r" (Read) mode and load the data!
with open("player_save.json", "r") as file:
    loaded_data = json.load(file)
    
# 🚨 MISSION 3: Print the loaded data!
print(f"Welcome back to the server: {loaded_data}")