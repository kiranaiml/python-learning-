#The Free Fire XP Combo Multiplier (Recursion)
def xp_multiplier(combo):
    if combo == 1:
        return 1
    else:
        return combo * xp_multiplier(combo - 1)
final_xp = xp_multiplier(4)
print(f"Total XP Multiplier: {final_xp}x")