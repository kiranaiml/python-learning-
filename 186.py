# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE SOCIAL MEDIA REEL
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are building the backend for a social media dashboard.
# You need a custom object that tracks an individual video 
# reel and has a built-in action to update its views when it 
# hits the algorithm.
# 
# SYSTEM REQUIREMENTS:
# 1. Create a class named `Reel`.
# 2. In the setup engine, accept `audio_track` and `views`.
#    Save both to the object.
# 3. Create a method called `hit_algorithm(self, new_views)`.
# 4. Inside the method, add the `new_views` to the object's `views`.
# 5. Outside the class, build a new object for a reel using 
#    "Kannada Rap" as the audio and 1000 as the starting views.
# 6. Call your method to add 50000 new views to the reel.
# 7. Print the reel's audio track and its updated total views 
#    using dot notation.
# 
# EXPECTED OUTPUT:
# Audio: Kannada Rap
# Total Views: 51000
# ---------------------------------------------------------
class reel:
    def __init__(self,audio_track,views):
        self.audio_track=audio_track
        self.views=views
    def hit_algorithm(self,new_views):
        self.views+=new_views
reels=reel("kannada Rap",1000)
reels.hit_algorithm(50000)
print(f"Audio :{reels.audio_track}\ntotal views : {reels.views}")