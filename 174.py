# ---------------------------------------------------------
# ⚡ THE SOLO CHALLENGE: THE ASYNC FETCHER (HARD)
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# Your backend needs to fetch data from 3 different databases. 
# If you do it normally, it takes 6 seconds (2s + 1s + 3s). 
# You must use asyncio to fetch them CONCURRENTLY so the entire 
# process only takes 3 seconds total.
# 
# THE REQUIREMENTS:
# 
# 1. Import the 'asyncio' library.
# 
# 2. THE WORKER:
#    - Write an asynchronous function: async def fetch_db(db_name, delay):
#    - Print: f"Initiating connection to {db_name}..."
#    - Pause execution for 'delay' seconds using asyncio's non-blocking sleep.
#    - Return the string: f"{db_name}_DATA"
# 
# 3. THE MANAGER:
#    - Write an asynchronous function: async def main():
#    - Use asyncio.gather() to run these 3 tasks AT THE SAME TIME:
#        Task 1: fetch_db("Users", 2)
#        Task 2: fetch_db("Orders", 1)
#        Task 3: fetch_db("Products", 3)
#    - Save the gathered results to a variable and print that list.
# 
# 4. THE EXECUTION:
#    - You cannot call main() normally. You must execute it 
#      using the standard asyncio run command.
# 
# EXPECTED OUTPUT:
# Initiating connection to Users...
# Initiating connection to Orders...
# Initiating connection to Products...
# ['Users_DATA', 'Orders_DATA', 'Products_DATA']
# ---------------------------------------------------------
import asyncio
async def fetch_db(db_name, delay):
    print(f"Initiating connection to {db_name}...")
    await asyncio.sleep(delay) 
    
    return f"{db_name}_DATA"
async def main():
    results = await asyncio.gather(
        fetch_db("Users", 2),
        fetch_db("Orders", 1),
        fetch_db("Products", 3)
    )
    print(results)
asyncio.run(main())