# ---------------------------------------------------------
# 🔀 THE SOLO CHALLENGE: THE SMART DISPATCHER
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# Combine your Decorator skills with your Match/Case skills! 
# Build a system that audits incoming network requests and 
# routes them to the correct action.
# 
# THE REQUIREMENTS:
# 
# 1. THE DECORATOR:
#    - Create a decorator named 'audit_log'.
#    - Inside the wrapper, print: "--- AUDIT: Processing request ---"
#    - Run the wrapped function and save the result.
#    - Print: "--- AUDIT: Request complete ---"
#    - Return the result.
# 
# 2. THE TARGET FUNCTION (The Engine):
#    - Target this function with your '@audit_log' decorator.
#    - Write a function called 'process_request(data)'. 
#    - Inside it, use 'match data:' to route the dictionary:
#       - Case 1: {"action": "login", "user": name} 
#                 Print: f"🟢 Logging in user: {name}"
#       - Case 2: {"action": "logout", "user": name} 
#                 Print: f"🔴 Logging out user: {name}"
#       - Case 3: The catch-all (_)
#                 Print: "⚠️ Unknown action."
# 
# 3. THE EXECUTION:
#    - Test your system by passing a dictionary into your function:
#      process_request({"action": "login", "user": "Kiran"})
# 
# EXPECTED OUTPUT:
# --- AUDIT: Processing request ---
# 🟢 Logging in user: Kiran
# --- AUDIT: Request complete ---
# ---------------------------------------------------------
def adiut_log(func):
    def wrapper(*args,**kwarge):
        print("--- AUDIT: Processing request ---")
        result=func(*args,**kwarge)
        print("--- AUDIT: Request complete ---")

        return result
    return wrapper
@adiut_log
def process_request(data):
    match data:
        case{"action": "login", "user": name} :
            print( f"🟢 Logging in user: {name}")
        case{"action": "logout", "user": name} :
                print(f"🔴 Logging out user: {name}")
        case _:
            print("⚠️ Unknown action.")

process_request({"action": "login", "user": "Kiran"})