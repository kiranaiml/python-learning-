# The logged-in user
current_user = {"name": "karthik", "is_admin": False}

# ==========================================
# ❌ THE MESSY SYSTEM (Violates the "Don't Repeat Yourself" rule)
# ==========================================
current_user = {"name": "karthik", "is_admin": False}

def require_admin(func):
    
    # This wrapper acts as the security guard
    def wrapper():
        if current_user["is_admin"] == False:print("🛑 ERROR: You are not an admin!")
        else:func
    return wrapper
class  delete_database:
    # ❌ They pasted this security check here...
    def current_user(self):
        print("🛑 ERROR: You are not an admin!")
        return

    print("💥 Database deleted!")

class  view_secret_financials(delete_database):
    # ❌ ...and they pasted the exact same check here!
    def current_user(self):
        print("🛑 ERROR: You are not an admin!")
        return

    print("💰 Company makes $1,000,000 a day.")

# Execution
delete_database()