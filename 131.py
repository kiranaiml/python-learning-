# =====================================================================
# 🛡️ LEVEL 2, QUESTION 2: The Incomplete Profile Loop
# =====================================================================
# 
# THE SCENARIO:
# You are pulling profiles from a database to send an email newsletter.
# You have a list of dictionaries, but one user forgot to provide their email!
# If Python tries to look up an 'email' that doesn't exist, it throws a KeyError.
# 
# YOUR MISSION:
# 1. Put the dictionary lookup INSIDE a `try` block within the loop.
# 2. Add an `except KeyError:` block. If it crashes, print:
#    f"Warning: No email found for {user['name']}. Skipping..."
# 3. Add an `else:` block that prints: f"Sending newsletter to: {email_address}"
# =====================================================================

user_database = [
    {"name": "Kiran", "email": "kiran@example.com"},
    {"name": "Ajay", "email": "ajay@example.com"},
    {"name": "Divakara"}, # 🚨 WARNING: Missing email key!
    {"name": "Bhoomika", "email": "bhoomika@example.com"}
]

print("--- Newsletter System Starting ---\n")

for user in user_database:
    # 🚨 FIX THIS LOGIC USING TRY/EXCEPT/ELSE INSIDE THE LOOP:  
    try:
        email_address = user["email"]
    except KeyError:
        print(f"Warning: No email found for {user['name']}. Skipping...")
    else:
        print(f"Sending newsletter to: {email_address}")
        print("\n--- Newsletter Run Complete ---")