# =====================================================================
# 🛡️ LEVEL 2, QUESTION 4: The Flawless Player Loop
# =====================================================================
# 
# YOUR MISSION:
# 1. Put the `kd_ratio = player["kills"] / player["deaths"]` math 
#    INSIDE a `try` block within the loop.
# 2. Add an `except ZeroDivisionError:` block. If it catches the zero, 
#    print: f"Wow! {player['name']} had a flawless game! (0 Deaths)"
# 3. Add an `else:` block that prints: 
#    f"{player['name']}'s K/D Ratio is: {kd_ratio}"
# =====================================================================

match_stats = [
    {"name": "Ajay", "kills": 12, "deaths": 4},
    {"name": "Divakara", "kills": 8, "deaths": 2},
    {"name": "Kiran", "kills": 15, "deaths": 0}, # 🚨 WARNING: 0 Deaths!
    {"name": "Yashu", "kills": 5, "deaths": 5}
]

print("--- Calculating Squad K/D Ratios ---\n")

for player in match_stats:
    # 🚨 FIX THIS MATH USING TRY/EXCEPT/ELSE INSIDE THE LOOP:
    try:
        kd_ratio = player["kills"] / player["deaths"]
    except ZeroDivisionError:
        print(f"Wow! {player['name']} had a flawless game! (0 Deaths)")
    else:
        print(f"{player['name']}'s K/D Ratio is: {kd_ratio}")
    
print("\n--- Stats Calculation Complete ---")