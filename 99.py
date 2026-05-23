#The Global Airline Engine
class ticket:
    def __init__(self, passenger_name, seat_number):
        self.passenger_name = passenger_name
        self.seat_number = seat_number
        self._price = 5000

    def get_details(self):
        return f"Passenger: {self.passenger_name}, Seat: {self.seat_number}, Price: {self._price}"
class economyticket(ticket):
    def __init__(self, passenger_name, seat_number):
        super().__init__(passenger_name, seat_number)

    def get_details(self):
        return super().get_details() + " [Economy Class]"
class fristclassticket(ticket):
    def __init__(self, passenger_name, seat_number):
        super().__init__(passenger_name, seat_number)
        self._price = 15000

    def get_details(self):
        return super().get_details() + " [First Class + Lounge Access]"

class flight:
    def __init__(self,flight_number,max_capacity):
        self.seat_map={}
        self.flight_number=flight_number
        self.max_capacity=max_capacity
    def book_seat(self,ticket):
        if len(self.seat_map)>=self.max_capacity:
            print(f"❌ Flight Full! Cannot book {ticket.passenger_name}.")
        elif ticket.seat_number in self.seat_map:
            print(f"❌ Seat {ticket.seat_number} is already taken!")
        else:
            self.seat_map[ticket.seat_number] = ticket
            print(f"✅ Booked {ticket.passenger_name} in seat {ticket.seat_number}.")
    def print_manifest(self):
        print(f"📋 --- Manifest for Flight {self.flight_number} ---")
        for seat, ticket in self.seat_map.items():
            print(ticket.get_details())

if __name__ == "__main__":
    # 1. Create a small flight (Capacity: Only 2 seats!)
    my_flight = flight("INDIGO-777", 2)
    
    # 2. Create the Tickets
    ticket1 = fristclassticket("Kiran", "1A")
    ticket2 = economyticket("Divakara", "1B")
    
    # Uh oh, someone is trying to steal seat 1A!
    ticket3 = economyticket("Karthik", "1A") 
    
    # Wait list passenger
    ticket4 = economyticket("Yashu", "2A")
    
    print("\n--- Booking Phase ---")
    my_flight.book_seat(ticket1) # Should succeed
    my_flight.book_seat(ticket3) # Should fail (Seat 1A taken)
    my_flight.book_seat(ticket2) # Should succeed
    my_flight.book_seat(ticket4) # Should fail (Flight capacity is 2)
    
    print("\n")
    my_flight.print_manifest()