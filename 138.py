# =====================================================================
# 🟡 LEVEL 6, QUESTION 2: The Safe Update (Append Mode)
# =====================================================================

print("--- Updating server logs ---")

# 🚨 FIX THIS LOGIC: Use Append Mode to protect the old data!
with open("trail.txt", "a") as file:
    
    # Add a new name, but put \n first so it goes to the next line!
    file.write("\nKushal")

print("--- Log successfully updated! ---")