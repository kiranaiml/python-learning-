# =====================================================================
# 🛡️ LEVEL 2, QUESTION 3: The Bad Input Loop
# =====================================================================
# 
# YOUR MISSION:
# 1. Put the `int(entry)` conversion INSIDE a `try` block.
# 2. Add an `except ValueError:` block. If it catches a word, print:
#    f"Warning: Invalid ID format -> '{entry}'. Skipping..."
# 3. Add an `else:` block that does TWO things:
#    - Appends the clean integer to the list: valid_ids.append(player_id)
#    - Prints a success message: f"Successfully registered ID: {player_id}"
# =====================================================================

# A batch of user inputs (Notice the third one is text!)
player_entries = ["1048573", "8493021", "karthik_Boss", "9384710"]

# We will store the successfully converted numbers here
valid_ids = []

print("--- Tournament Registration Starting ---\n")

for entry in player_entries:
    # 🚨 FIX THIS LOGIC USING TRY/EXCEPT/ELSE INSIDE THE LOOP:
    try:    
        player_id = int(entry)
    except ValueError:
        print(f"Warning: Invalid ID format -> '{entry}'. Skipping...")
    else:
        valid_ids.append(player_id)
        print(f"Successfully registered ID: {player_id}")
    # Hint: Don't forget to append it to valid_ids if it succeeds!

print(f"\n--- Final Clean Roster: {valid_ids} ---")