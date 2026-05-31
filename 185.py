# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE PLAYER ACTIONS
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are building the profile system for a mobile battle royale. 
# You need a custom object that stores a player's score and has 
# a built-in action to increase that score when they win a match.
# 
# SYSTEM REQUIREMENTS:
# 1. Create a class named `Player`.
# 2. In the `__init__` engine, accept `username` and `score`. 
#    Save them using `self.username` and `self.score`.
# 3. Create a NEW method inside the class called `add_points(self, points)`.
# 4. Inside `add_points`, add the new `points` to `self.score`.
# 5. OUTSIDE the class, build a player named "Kiran" with a 
#    starting score of 100. Save it to a variable (e.g., `player_one`).
# 6. Call the method to give the player 50 more points. 
#    (Hint: `player_one.add_points(50)`)
# 7. Print the player's final score using dot notation.
# 
# EXPECTED OUTPUT:
# Final Score: 150
# ---------------------------------------------------------
class player:
    def __init__(self,username,score):
        self.username=username
        self.score=score
    def add_point(self,points):
        self.score+=points
player_one=player("kiran",100)
player_one.add_point(50)
print(f"player score: {player_one.score}")
