# A messy, real-world data stream
live_feed = [
    {"alert": "trade", "symbol": "TATA", "price": 1050},
    ["system", "backup_complete"],
    "connection_test",
    {"alert": "error", "code": 503, "details": "Timeout"}
]

for data in live_feed:
    match data:
        case {"alert": "trade", "symbol": symbol, "price": price}:
            print(f"TRADE EXECUTED: {symbol} at ₹{price}")
        case ["system", status]:
             print(f"SYSTEM LOG: {status}")
        case "connection_test":
            print("Test successful. Systems online.")
        case _:
            print("Unknown data format received.")