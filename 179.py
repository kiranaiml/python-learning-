# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE HIGHWAY RIDER
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are tracking the distance of a multi-day motorcycle tour. 
# Some days you rode long highway stretches, some days were short 
# local trips, and one day you just rested. You need a system to 
# analyze your riding data.
# 
# THE INPUT DATA:
# ride_distances = [120, 210, 85, 0, 160, 240, 45]
# 
# SYSTEM REQUIREMENTS:
# 1. Calculate the 'Total Distance' covered over the entire trip.
# 2. Count exactly how many 'Long Rides' you had (only count 
#    the days where you rode strictly greater than 150 kilometers).
# 3. Print the Total Distance and the number of Long Rides.
# 
# EXPECTED OUTPUT:
# Total Distance: 860
# Long Rides: 3
# ---------------------------------------------------------
ride_distance=[120,210,85,0,160,45]
total_distance=0
long_ride=0
for ride in ride_distance:
    if ride>0:
        total_distance+=ride
    if ride>100:
        long_ride+=1
print(f"Total distance : {total_distance}\n Long ride : {long_ride}")