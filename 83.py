#The Free Fire Squad Tracker (List of Dictionaries)
squad=[
    {
        "name": "kushal",
        "kills": 12
    },
    {
        "name": "karthik",
        "kills": 8
    }
]
total_kills = 0
for player in squad:
    total_kills+=player["kills"]
    print(f"-{player['name']} got {player['kills']} kills!")
print(f"Total kills by the squad: {total_kills}")