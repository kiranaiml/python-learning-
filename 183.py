# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE MATCH SCORE ENGINE
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are programming the post-match screen for a battle royale 
# game. You need a reusable tool (Function) that calculates a 
# player's total score based on two things: how many kills they 
# got, and how many minutes they survived.
# 
# THE MATH RULES:
# - Every kill is worth 50 points.
# - Every minute survived is worth 10 points.
# 
# SYSTEM REQUIREMENTS:
# 1. Define a function named `calculate_score` that takes TWO 
#    parameters: `kills` and `survival_minutes`.
# 2. Inside the function, calculate the total points using the 
#    math rules above. Save it in a bucket (like `total_score`).
# 3. Use the `return` keyword to spit the `total_score` out.
# 4. OUTSIDE the function, test your new engine! Call the function 
#    for a player named Muruli who had 4 kills and survived for 15 minutes.
# 5. Print the result directly so you catch the answer.
# 
# EXPECTED OUTPUT:
# Muruli's Match Score: 350
# ---------------------------------------------------------
def calculate_score(kills,survival_minutes):
    total_score=kills*50+survival_minutes*10
    return total_score
print(f"Kushal's match score:{calculate_score(4,23)}")