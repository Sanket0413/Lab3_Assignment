class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        matching_flights = []
        for flight in self.flights:
            if flight.from_city == city or flight.to_city == city:
                matching_flights.append(flight)
        return matching_flights

    def search_by_from_to_cities(self, from_city, to_city):
        matching_flights = []
        for flight in self.flights:
            if flight.from_city == from_city and flight.to_city == to_city:
                matching_flights.append(flight)
        return matching_flights

def print_flights(flights):
    if not flights:
        print("No flights found.")
    else:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in flights:
            print(f"{flight.flight_id}\t{flight.from_city}\t{flight.to_city}\t{flight.price}")

def main():
    flight_table = FlightTable()
    
    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]
    
    for data in flight_data:
        flight = Flight(*data)
        flight_table.add_flight(flight)
    
    while True:
        print("\nSearch options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            city = input("Enter the city: ")
            matching_flights = flight_table.search_by_city(city)
            print_flights(matching_flights)
        elif choice == "2":
            city = input("Enter the city: ")
            matching_flights = flight_table.search_by_city(city)
            print_flights(matching_flights)
        elif choice == "3":
            from_city = input("Enter the source city: ")
            to_city = input("Enter the destination city: ")
            matching_flights = flight_table.search_by_from_to_cities(from_city, to_city)
            print_flights(matching_flights)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()