# ---------------------------------------------------------
# 🟡 THE SOLO CHALLENGE: THE PENDING TASK BATCHER (MEDIUM)
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You have a massive list of database records. You want to 
# pull out and process only the records marked "pending", 
# one at a time, to save memory.
# 
# THE DATA:
# 
# 
# THE REQUIREMENTS:
# 
# 1. THE GENERATOR FUNCTION:
#    - Create a function named 'pending_task_generator(task_list)'.
#    - Write a standard 'for' loop to iterate through the 'task_list'.
#    - Inside the loop, check IF the task's "status" is "pending".
#    - If it is, use 'yield' to hand back the task's "id".
# 
# 2. THE EXECUTION:
#    - Create your generator object: my_gen = pending_task_generator(tasks)
#    - Instead of typing next() manually, use a 'for' loop outside 
#      the function: 'for task_id in my_gen:'
#    - Inside that loop, print: f"Processing task ID: {task_id}"
# 
# EXPECTED OUTPUT:
# Processing task ID: 2
# Processing task ID: 3
# Processing task ID: 5
# ---------------------------------------------------------
tasks = [
    {"id": 1, "status": "done"},
     {"id": 2, "status": "pending"},
    {"id": 3, "status": "pending"},
    {"id": 4, "status": "done"},
    {"id": 5, "status": "pending"}
]
def pending_task_generation(tasks_list):
    for task in tasks_list:                      
        if task["status"] == "pending":          
            yield task["id"]
my_gen=pending_task_generation(tasks)
for task_id in my_gen:
    print(f"Processing task ID:{task_id}")