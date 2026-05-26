# =====================================================================
# 🛡️ LEVEL 1, QUESTION 5: The Data Mismatch Crash (TypeError)
# =====================================================================
# 
# THE SCENARIO:
# You are calculating the total distance of your road trip. 
# Day 1 was 150 km (an integer). Day 2 came from a text file as "100" (a string).
# Python crashes with a TypeError when you try to add a number and text together!
# 
# YOUR MISSION:
# 1. Put the vulnerable addition AND print statement inside a `try` block.
# 2. Add an `except TypeError:` block. If it crashes, print exactly: 
#    "Error: Cannot add numbers and text together!"
# 3. Add an `else:` block. If it succeeds, print: 
#    "Distance calculated successfully!"
# 4. Add a `finally:` block that always prints: 
#    "--- Mileage Tracker Closed ---"
# =====================================================================

day_1_km = 150
day_2_km = "100" # Notice the quotes. This is a string!
total=[]

try:
    print(f"Total distance: {total(day_1_km+day_2_km)}")
except TypeError:
    print("Error: Cannot add numbers and text together!")
else:
    print("Distance calculated successfully!")
finally:
    print("--- Mileage Tracker Closed ---")