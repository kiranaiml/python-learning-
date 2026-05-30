# ---------------------------------------------------------
# 👑 THE FINAL BOSS: THE ASYNC SIP ENGINE (MASTER TIER)
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You are building the backend for a daily SIP tracker. 
# You need to pull live data for 3 funds concurrently, 
# generate a memory-efficient stream of daily ₹500 investments, 
# and calculate the total invested using functional programming.
# 
# THE REQUIREMENTS:
# 
# 1. THE IMPORTS:
#    - Bring in the 'asyncio' library.
#    - Bring in 'reduce' from the 'functools' library.
# 
# 2. THE ASYNC WORKER (Concurrency):
#    - Create: async def fetch_nav(fund_name):
#    - Await a 1-second sleep (simulating network delay).
#    - Return the string: f"🟢 {fund_name} NAV Connected"
# 
# 3. THE GENERATOR (Memory Efficiency):
#    - Create: def sip_generator(days):
#    - Write a loop that runs for the number of 'days' specified.
#    - Inside the loop, yield the integer: 500
# 
# 4. THE MASTER MANAGER:
#    - Create: async def main():
#    
#    -- PART A: The Async Fetch --
#    - Use asyncio.gather() to fetch these 3 funds at the SAME TIME:
#      "Bandhan Small Cap", "Parag Parikh Flexi", "Tata Silver ETF".
#    - Print the resulting list of connections.
# 
#    -- PART B: The Functional Math --
#    - Call your generator to simulate 5 days: 
#      my_sips = list(sip_generator(5))
#    - Use reduce() and a lambda function to add up all the numbers 
#      inside 'my_sips' into a variable called 'total_invested'.
#    - Print: f"Total Invested this week: ₹{total_invested}"
# 
# 5. THE IGNITION:
#    - Boot up the main function using the proper asyncio run command.
# 
# EXPECTED OUTPUT:
# ['🟢 Bandhan Small Cap NAV Connected', '🟢 Parag Parikh Flexi NAV Connected', '🟢 Tata Silver ETF NAV Connected']
# Total Invested this week: ₹2500
# ---------------------------------------------------------
import asyncio
from functools import reduce

async def fetch_nav(fund_name):
    await asyncio.sleep(1) 
    return f"🟢 {fund_name} NAV Connected"
def sip_generator(days):
    for _ in range(days):
        yield 500
async def main():
    results = await asyncio.gather(
        fetch_nav("Bandhan Small Cap"),
        fetch_nav("Parag Parikh Flexi"),
        fetch_nav("Tata Silver ETF")
    )
    print(results)
    my_sip = list(sip_generator(5))
    total_invested = reduce(lambda x, y: x + y, my_sip)
    print(f"Total Invested this week: ₹{total_invested}")
asyncio.run(main())
