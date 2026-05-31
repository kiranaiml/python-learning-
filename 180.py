# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE CONSTRUCTION ESTIMATOR
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are calculating the construction costs for an eco-modern 
# architectural project. You have a dictionary where the "Key" 
# is the material (like timber or glass) and the "Value" is the 
# cost in rupees. You need to analyze the budget.
# 
# THE INPUT DATA:
# material_costs = {
#     "Timber": 45000,
#     "Glass Panels": 28000,
#     "Eco-Concrete": 32000,
#     "Solar Tiles": 55000,
#     "Steel Framing": 40000
# }
# 
# SYSTEM REQUIREMENTS:
# 1. Calculate the 'Total Budget' needed for all materials combined.
# 2. Count exactly how many 'Premium Materials' you are using 
#    (any material that costs strictly greater than 35000).
# 3. Print the Total Budget and the Premium Materials count.
# 
# EXPECTED OUTPUT:
# Total Budget: 200000
# Premium Materials: 3
# ---------------------------------------------------------
material_costs={
    "timber":45000,
    "glass panels":28000,
    "eco-concrete":32000,
    "solar tiles":55000,
    "steel framing":40000
}
total_buget=0
premium_material=0
for buget in material_costs.values():
    if buget>35000:
        premium_material+=buget
        total_buget+=1
print(f"\nPremium materials :{premium_material}\nTotal Budget:{total_buget}")