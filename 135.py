# =====================================================================
# 🏗️ LEVEL 4, QUESTION 1: The Player Blueprint
# =====================================================================
# 
# YOUR MISSION:
# 1. Inside the `__init__` method, save the `name` and `rank` parameters 
#    to the object using `self`. (e.g., self.name = name)
# 2. At the bottom, build a new player object named "Muruli_Boss" 
#    with the rank "Heroic". Save it to a variable called `player1`.
# 3. Print the new player's stats by asking the object for its data!
# =====================================================================

class Player:
    def __init__(self, name, rank):
        # ✅ MISSION 1: Flawless execution.
        self.name = name
        self.rank = rank

print("--- Initializing Game Server ---\n")

# ✅ MISSION 2: Call the actual Player blueprint!
player1 = Player("kushal", "Heroic")

# ✅ MISSION 3: Use the "dot" to ask the object for its internal data.
print(f"New Player Joined -> {player1.name} [{player1.rank}]")