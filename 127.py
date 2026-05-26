#error , except, else and finally handling


playlist = ["Hip Hop Mix", "Techno Beats", "Modern Bollywood"]

try:
    print(f'playing: {playlist}')

except IndexError:
    print("Error: That song number does not exist!")

else:
    print("Song loaded successfully! Turn up the volume.")

finally:
    print("--- Playlist Check Finished ---")