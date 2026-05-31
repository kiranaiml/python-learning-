# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE SOCIAL MEDIA ANALYZER
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You need to generate a performance report for an Instagram 
# account. You have the view counts for various reels, and you 
# need to find the total reach and count how many reels went "viral".
# 
# THE INPUT DATA:
# reel_views = {
#     "hip_hop_dance": 15000,
#     "techno_beats": 8000,
#     "bollywood_transition": 55000,
#     "kannada_rap": 102000,
#     "nature_vlog": 4500
# }
# 
# SYSTEM REQUIREMENTS:
# 1. Calculate the 'Total Views' across all reels combined.
# 2. Count exactly how many 'Viral Reels' you have (any reel 
#    that has strictly greater than 50000 views).
# 3. Print the Total Views and the Viral Reels count.
# 
# EXPECTED OUTPUT:
# Total Views: 184500
# Viral Reels: 2
# ---------------------------------------------------------
reel_view={
    "hip_hop_dance":15000,
    "techno_beats":8000,
    "bollywood_transition":55000,
    "kannada_rap":102000,
    "nature_vlog":4500
}
total_views=0
viral_reels=0
for reach in reel_view.values():
    total_views+=reach
    if reach>50000:
        viral_reels+=1
print(f"total views:{total_views}\nviral reels : {viral_reels}")