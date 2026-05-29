# ---------------------------------------------------------
# 🎁 THE SOLO CHALLENGE: THE ANNOUNCER (EASY)
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You want a simple way to know exactly when any function 
# starts running and when it finishes. 
# 
# THE REQUIREMENTS:
# 
# 1. THE DECORATOR:
#    - Create a decorator named 'announce'.
#    - Inside its wrapper, print exactly: "--- Starting function ---"
#    - Run the wrapped function.
#    - After the function runs, print exactly: "--- Function complete ---"
# 
# 2. THE TARGET FUNCTION:
#    - Write a basic function called 'say_hello()'. 
#    - Inside it, simply print: "Hello, Architect!"
# 
# 3. THE EXECUTION:
#    - Attach your '@announce' decorator to the target function.
#    - Call say_hello() at the bottom of your file.
# 
# EXPECTED OUTPUT:
# --- Starting function ---
# Hello, Architect!
# --- Function complete ---
# ---------------------------------------------------------
def announce(func):
    def wrapper(*args,**kwargs):
        print("----Starting function---")
        result=func(*args,**kwargs)
        print("---Function complete---")
        return result
    return wrapper
@announce
def say_hello():
    print("Hello, Architect!")
say_hello()