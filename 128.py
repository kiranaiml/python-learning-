# =====================================================================
# 🛡️ LEVEL 1, QUESTION 4: The Typo Crash (NameError)
# =====================================================================
# 
# THE SCENARIO:
# You calculated the final amount, but when you went to print it, 
# you misspelled the variable name (final_amont instead of final_amount).
# This causes Python to throw a NameError because it doesn't recognize the word!
# 
# YOUR MISSION:
# 1. Put the vulnerable print statement inside a `try` block.
# 2. Add an `except NameError:` block. If it crashes, print exactly: 
#    "Error: You used a variable that doesn't exist!"
# 3. Add an `else:` block. If it succeeds, print: 
#    "Calculation successful!"
# 4. Add a `finally:` block that always prints: 
#    "--- Bot Shutdown ---"
# =====================================================================

final_amount = 50000

try:
    print(f"Final amount: {final_amount}")
except NameError:
    print("Error: You used a variable that doesn't exist!")
else:
    print("Calculation successful!")
finally:
    print("--- Bot Shutdown ---")