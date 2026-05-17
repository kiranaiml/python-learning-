#The Business Rules
total_account_views=0
def upload_reel(reel_name, view_count):
    global total_account_views
    total_account_views += view_count
    estimated_likes=view_count/10
    print(f"Dropped:{reel_name}|Views:{view_count}|Estimated Likes: {estimated_likes}")
upload_reel(reel_name="Kannada Hip Hop mix",view_count=5000)
upload_reel(reel_name="Modern Bollywood Transition",view_count=12000)
print(f"\nTotal Account Views: {total_account_views}")