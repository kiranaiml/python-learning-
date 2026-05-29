# A list of fake voice commands coming into our hub
incoming_commands = [
    ["lights", "living room", "on"],
    ["music", "pause"],
    ["lights", "bedroom", "off"],
    ["blender", "start"]
]

for command in incoming_commands:
    match command:
        case ["lights", room, action]:
            print(f"Turning {action} the {room} lights.")
        case ["music", action]:
            print(f"Music system is now set to: {action}.")
        case _:
            print(f"Command not recognized: {command}")
