#The Reel Music Selector
track_lists=[]
while True:
    track=input("Enter a track genre (or type 'finish' to stop):")
    if track=="finish":
        print("playlist complete!")
        break
    elif track=="ad" or track=="podcast":
        print("Skipping non-music audio...")
        continue
    else:
        track_lists.append(track)
        print("Track saved.")
print(f"\nFinal reel Playlist:{track_lists}")