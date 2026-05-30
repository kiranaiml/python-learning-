# ---------------------------------------------------------
# 🔴 THE SOLO CHALLENGE: THE SENSOR PIPELINE (HARD)
# ---------------------------------------------------------
# 
# THE BUSINESS GOAL:
# You are programming the safety backend for a factory's 
# CNC machine. You must build a pipeline where the hardware 
# generator feeds data directly into a software generator.
# 
# THE DATA:
# raw_temps = [75, 82, 88, 95, 102, 85]
# 
# THE REQUIREMENTS:
# 
# 1. GENERATOR 1 (The Hardware):
#    - Create a function: def read_sensor(temp_list):
#    - Write a simple 'for' loop to iterate through 'temp_list'.
#    - yield each temperature one by one.
# 
# 2. GENERATOR 2 (The Software Monitor):
#    - Create a function: def safety_monitor(sensor_data):
#    - Write a 'for' loop to iterate through 'sensor_data'.
#      (Mind-bending part: 'sensor_data' will be your first generator!)
#    - Inside the loop, check the temperature:
#      - IF it is 90 or higher, yield: f"🚨 OVERHEAT: {temp}C"
#      - ELSE, yield: f"🟢 Normal: {temp}C"
# 
# 3. THE EXECUTION:
#    - Prime the hardware: hardware_gen = read_sensor(raw_temps)
#    - Prime the software: 
#    
#    - Finally, use a standard 'for' loop to iterate through 
#      'monitor_gen' and print out every alert!
# 
# EXPECTED OUTPUT:
# 🟢 Normal: 75C
# 🟢 Normal: 82C
# 🟢 Normal: 88C
# 🚨 OVERHEAT: 95C
# 🚨 OVERHEAT: 102C
# 🟢 Normal: 85C
# ---------------------------------------------------------
raw_temps = [75, 82, 88, 95, 102, 85]
def read_sensor(temp_list):
    for temp in temp_list:
        yield temp
def safety_monitor(sensor_data):
    for sensor in sensor_data:
        if sensor >=90:
            yield f"🚨 overheat:{sensor}C"
        else:
            yield f"🟢Normal:{sensor}C"
hardware_gen = read_sensor(raw_temps)
monitor_gen = safety_monitor(hardware_gen)
for gen in monitor_gen:
    print("print out every alert!")