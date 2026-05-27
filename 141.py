import json

# --- SERVER SETUP: Creating the initial save file ---
initial_data = {"username": "Kiran", "coins": 100}
with open("vault.json", "w") as f:
    json.dump(initial_data, f)
print("--- Server Online. Starting Balance: 100 Coins ---\n")

# =====================================================================
# 🟠 LEVEL 7: The Medium Challenge (Read -> Modify -> Write)
# =====================================================================

print("Incoming Deposit: 500 Coins...")

# 🚨 1. READ: Open the file in Read Mode and load the JSON data
with open("vault.json", "r") as file:
    player_data = json.load(file)

# 🚨 2. MODIFY: Update the dictionary in temporary memory
player_data["coins"] = player_data["coins"] + 500

# 🚨 3. WRITE: Open the file in Write Mode and dump the updated data back!
with open("vault.json", "w") as file:
    json.dump(player_data, file)

print(f"Transaction Complete! Permanent Balance: {player_data['coins']} Coins")