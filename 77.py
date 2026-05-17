# The Squad Lobby Builder

def launch_match(*players, **settings):
    
    for player in players:
        print(f"Player joined: {player}")
        
    for key, value in settings.items():
        print(f"Match Setting -> {key}: {value}")

launch_match("kruthika", "karthik", "kushal", "janavi", map="Bermuda", mode="Ranked")