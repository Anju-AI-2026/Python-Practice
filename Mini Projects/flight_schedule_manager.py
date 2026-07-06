# Mini Project: Flight Schedule Manager

flights = []

while True:
    print("\n===== FLIGHT SCHEDULE MANAGER =====")
    print("1. Add Flight")
    print("2. Display Flights")
    print("3. Search Flight")
    print("4. Remove Flight")
    print("5. Count Flights")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        flight_number = input("Enter flight number: ")
        destination = input("Enter destination: ")
        departure_time = input("Enter departure time: ")

        flight = (flight_number, destination, departure_time)
        flights.append(flight)

        print("Flight added successfully.")

    elif choice == 2:
        if len(flights) == 0:
            print("No flights available.")
        else:
            print("\n===== FLIGHT SCHEDULE =====")

            # Display all flight details
            for flight in flights:
                print(f"\nFlight Number : {flight[0]}")
                print(f"Destination   : {flight[1]}")
                print(f"Departure     : {flight[2]}")

    elif choice == 3:
        flight_number = input("Enter flight number to search: ")

        found = False

        # Search for the flight
        for flight in flights:
            if flight[0] == flight_number:
                print("\nFlight Found")
                print(f"Destination : {flight[1]}")
                print(f"Departure  : {flight[2]}")
                found = True
                break

        if not found:
            print("Flight not found.")

    elif choice == 4:
        flight_number = input("Enter flight number to remove: ")

        found = False

        # Remove the selected flight
        for flight in flights:
            if flight[0] == flight_number:
                flights.remove(flight)
                print("Flight removed successfully.")
                found = True
                break

        if not found:
            print("Flight not found.")

    elif choice == 5:
        print(f"Total Flights: {len(flights)}")

    elif choice == 6:
        print("Thank you for using Flight Schedule Manager.")
        break

    else:
        print("Invalid choice.")
