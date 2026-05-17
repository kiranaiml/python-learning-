# 1. THE SETUP
match_scores = [1200, 450, 3100, 800, 2500]

bonus_xp = [match for match in match_scores if match > 1000]

def distribute_rewards(xp_list):
    for xp in xp_list:
        # Added the proper spaces inside the string!
        print(f"Awarding {xp} Bonus XP to pro player!")


distribute_rewards(bonus_xp)