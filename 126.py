config_data = {
    "host": "localhost",
    "port": 8080,
    "username": "admin"
}

print("--- Loading Server Config ---")

# 1. THE DANGER ZONE
try:
    print(f"Password is: {config_data['database_password']}")

# 2. THE SAFETY NET
except KeyError:
    print("Error: Password key is missing!")

# 3. THE VICTORY LAP
else:
    print("Password loaded successfully!")

# 4. THE CLEANUP CREW
finally:
    print("--- Config Check Finished ---")