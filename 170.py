# ---------------------------------------------------------
# 🔋 THE SOLO CHALLENGE: THE INFINITE ID GENERATOR
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You are building the backend for a high-traffic e-commerce store. 
# You need a fast, memory-efficient way to generate unique Order IDs 
# sequentially without ever running out of numbers.
# 
# THE REQUIREMENTS:
# 
# 1. THE GENERATOR FUNCTION:
#    - Create a function named 'order_id_generator()'.
#    - Inside it, create a variable called 'count' that starts at 1.
#    - Create an infinite loop using 'while True:'.
#    - Inside the loop, use the 'yield' keyword to hand back an 
#      f-string formatted like this: f"ORD-{count}"
#    - Right after the yield, add 1 to 'count'.
# 
# 2. THE EXECUTION:
#    - Outside the function, initialize your generator object: 
#      id_gen = order_id_generator()
#    - Simulate 3 customers checking out by using 'next(id_gen)' 
#      three separate times, and print each result.
# 
# EXPECTED OUTPUT:
# ORD-1
# ORD-2
# ORD-3
# ---------------------------------------------------------
def order_id_generator():
    count=1
    while True:
        yield f"ORD-{count}"
        count+=1
id_gen=order_id_generator()
print(next(id_gen))
print(next(id_gen))
print(next(id_gen))