#i am learned oop concpet , condtructer this concpet
# Instagram reel Tracker
class Reel:
    def __init__(self,song_name,views=0):
        self.views=views
        self.song_name=song_name
    def play_video(self):
        print(f"PLaying a reel with the song : {self.song_name}. It has  {self.views}!")
reel1=Reel("Modern Bollywood Mix")
reel2=Reel("Techno Beat",500)
reel1.play_video()
reel2.play_video()