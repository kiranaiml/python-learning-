#The Cinema Booking Matrix
seating_chart = [
    ["Taken", "Empty", "Taken"],
    ["Empty", "Empty", "Taken"],
    ["Taken", "Taken", "Empty"]
]
for row_index,row_data in enumerate(seating_chart):
    for seat_index,seat_status in enumerate(row_data):
        if seat_status=="Empty":
            print(f"Row {row_index},seat[{seat_index}] is AVAILABLE.")
        else:
            print(f"Row {row_index},seat[{seat_index}] is occupied.")
print(f"\nFull theater sacn completed.")
