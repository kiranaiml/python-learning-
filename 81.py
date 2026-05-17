#The Free Fire Player Database
player_profile={
    "username": "kushal",
    "level": 42,
    "rank": "Heroic",
    "diamonds": 150,
}
player_profile["diamonds"] -= 50
player_profile["level"] += 1
print(f"player {player_profile['username']} | Rank: {player_profile["rank"]} | Diamonds Left: {player_profile["diamonds"]}")