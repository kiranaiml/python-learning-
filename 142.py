# =====================================================================
# 📜 SIDE QUEST: The Server Error Log (Append Practice)
# =====================================================================
import datetime

# This grabs the actual current time from your computer!
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
error_message = f"\n[{current_time}] ERROR: Database connection failed!"

print("--- Server Warning Triggered ---")

# 🚨 MISSION 1: Open "server_logs.txt" in Append ("a") mode.
# 🚨 MISSION 2: Write the `error_message` variable to the file.
with open("trail.txt", "a") as file:
    file.write(error_message)

print("--- Error safely logged to hard drive ---\n")

# 🚨 MISSION 3: Open the file in Read ("r") mode, read the data, and print it!
with open("trail.txt", "r") as file:
    logs = file.read()
    print("--- Current Server Logs ---")
    print(logs)