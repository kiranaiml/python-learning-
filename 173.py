# ---------------------------------------------------------
# 🛡️ THE SOLO CHALLENGE: THE AUTO-LOCKING VAULT
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You need to connect to a secure database. You want a system 
# that automatically opens the connection, hands it to you, 
# and then automatically closes it the exact second you are 
# done—even if you forget!
# 
# THE REQUIREMENTS:
# 
# 1. THE SETUP:
#    - Import 'contextmanager' from the 'contextlib' library:
#      from contextlib import contextmanager
# 
# 2. THE GENERATOR:
#    - Create a function called 'secure_connect(db_name)'.
#    - Decorate it with exactly this: @contextmanager
#    
# 3. THE LIFECYCLE (Inside the function):
#    - The Setup: Print f"🔓 Opening secure connection to {db_name}..."
#    - The Handoff: yield a fake connection string like "CONN_OBJ_42"
#    - The Teardown: Print f"🔒 Closing connection to {db_name}. Vault locked."
# 
# 4. THE EXECUTION:
#    - You do NOT call this function normally. You use a 'with' block!
#    - Write this exactly: 
#      with secure_connect("Customer_DB") as conn:
#          print(f"Working inside database with: {conn}")
# 
# EXPECTED OUTPUT:
# 🔓 Opening secure connection to Customer_DB...
# Working inside database with: CONN_OBJ_42
# 🔒 Closing connection to Customer_DB. Vault locked.
# ---------------------------------------------------------
from contextlib import contextmanager
@contextmanager
def secure_connect(db_name):
    print(f"🔓Opening secure connection to{db_name}...")
    yield f"CONN_OBJ_42"
    print(f"🔓Closing connection to {db_name}. Vault locked")
with secure_connect("Customer_db") as conn:
        print(f"Working inside database with:{conn}")
    