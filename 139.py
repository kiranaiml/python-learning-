# =====================================================================
# 🔵 LEVEL 6, QUESTION 3: The Viewer (Read Mode)
# =====================================================================

print("--- Fetching Server Logs ---\n")

# 🚨 FIX THIS LOGIC: Open the file in Read Mode!
with open("trail.txt", "r") as file:
    
    # Grab the data inside the file and save it to a variable
    server_logs = file.read()
    
    # Print the variable to the screen!
    print("Server log")

print("\n--- Log Fetch Complete ---")