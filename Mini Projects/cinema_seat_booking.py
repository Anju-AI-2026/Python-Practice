# Mini Project: Cinema Seat Booking System

seats = [
    ["A1", "A2", "A3", "A4"],
    ["B1", "B2", "B3", "B4"],
    ["C1", "C2", "C3", "C4"]
]

while True:
    print("\n===== CINEMA SEAT BOOKING SYSTEM =====")
    print("1. Show Seats")
    print("2. Book Seat")
    print("3. Cancel Booking")
    print("4. Available Seats")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nCurrent Seat Layout\n")

        # Display all seats
        for row in seats:
            for seat in row:
                print(f"{seat:<5}", end="")
            print()

    elif choice == "2":

        seat_number = input("Enter seat number to book: ").upper()

        found = False

        # Book the selected seat
        for row in seats:
            for i in range(len(row)):
                if row[i] == seat_number:
                    row[i] = "XX"
                    found = True
                    print("Seat booked successfully.")

        if not found:
            print("Seat not available.")

    elif choice == "3":

        seat_number = input("Enter seat number to cancel (Example: A1): ").upper()

        found = False

        # Cancel booking
        for row_index in range(len(seats)):
            for col_index in range(len(seats[row_index])):

                expected = chr(65 + row_index) + str(col_index + 1)

                if expected == seat_number and seats[row_index][col_index] == "XX":
                    seats[row_index][col_index] = expected
                    found = True
                    print("Booking cancelled successfully.")

        if not found:
            print("Booked seat not found.")

    elif choice == "4":

        count = 0

        # Count available seats
        for row in seats:
            for seat in row:
                if seat != "XX":
                    count += 1

        print(f"Available Seats: {count}")

    elif choice == "5":
        print("Thank you for using Cinema Seat Booking System.")
        break

    else:
        print("Invalid choice.")
