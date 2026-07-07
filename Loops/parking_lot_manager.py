# Program to manage a small parking lot

parking = []

while True:

    print("\n===== PARKING LOT MANAGER =====")
    print("1. Park Vehicle")
    print("2. Show Parked Vehicles")
    print("3. Remove Vehicle")
    print("4. Count Vehicles")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        vehicle = input("Enter vehicle number: ").upper()
        parking.append(vehicle)
        print("Vehicle parked successfully.")

    elif choice == "2":

        if len(parking) == 0:
            print("Parking lot is empty.")
        else:
            print("\nParked Vehicles")

            for index, vehicle in enumerate(parking, start=1):
                print(f"{index}. {vehicle}")

    elif choice == "3":

        vehicle = input("Enter vehicle number to remove: ").upper()

        if vehicle in parking:
            parking.remove(vehicle)
            print("Vehicle removed successfully.")
        else:
            print("Vehicle not found.")

    elif choice == "4":

        print(f"Total Vehicles: {len(parking)}")

    elif choice == "5":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")
