# the game score
player_name=input("player name: ")
current_level=int(input("current year: "))
gold_pieces=int(input("gold pieces: ")) 
score=(current_level*50)+gold_pieces
level_progress=round((score/1000)*100)

game_tag=player_name[0:2].upper()
tag= game_tag+str(current_level)

print(f" player {tag},your score is {score} and you are {level_progress}% to the next rank! ")
