# =====================================================================
# 🛡️ LEVEL 2, QUESTION 1: The Corrupted Data Loop
# =====================================================================
# 
# YOUR MISSION:
# 1. Put the `total += amount` math INSIDE a `try` block.
#    (Make sure the try block is indented inside the for-loop!)
# 2. Add an `except TypeError:` block. If it catches corrupted data, 
#    print: f"Warning: Skipping corrupted data -> {amount}"
# 3. Add an `else:` block that prints: f"Processed ₹{amount}"
# 
# THE TRICK: If you do this right, the loop will skip the errors 
# and successfully add up the real numbers (200 + 150 + 300 + 50 = 700).
# =====================================================================

transactions = [200, 150, "ERROR", 300, "CORRUPT", 50]
total = 0

print("--- Starting Transaction Processor ---")

# Python automatically grabs the items one by one and calls them 'amount'
for amount in transactions:
    
    # 🛡️ THE SAFETY NET IS INSIDE THE LOOP!
    try:
        # We try to do the math...
        total += amount 
        
    except TypeError:
        # If the 'amount' was text, it crashes, and we catch it here!
        print(f"Warning: Skipping corrupted data -> {amount}")
        
    else:
        # If the math worked perfectly, we print this!
        print(f"Processed ₹{amount}")

# This is outside the loop, so it only prints once at the very end
print(f"\n--- Final Total Processed: ₹{total} ---")