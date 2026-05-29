incoming_responses = [
    {"status": 200, "data": "Sensex is up 500 points"},
    {"status": 500, "error": "Database connection failed"},
    {"status": 404},
    {"status": 200, "data": "Gold prices dropped"}
]

for response in incoming_responses:
    match response:
        case {"status":200,"data":data}:
         print(f"Success! Data received: {data}")
        case {"status":500,"error":error}:
          print(f"Server Crash! Reason: {error}")
        case _:
          print("Unknown response format.")