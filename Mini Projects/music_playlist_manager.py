# Mini Project: Music Playlist Manager

playlist = []

while True:
    print("\n===== MUSIC PLAYLIST MANAGER =====")
    print("1. Add Song")
    print("2. Display Playlist")
    print("3. Search Song")
    print("4. Remove Song")
    print("5. Count Songs")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        song = input("Enter song name: ")
        playlist.append(song)
        print("Song added successfully.")

    elif choice == 2:
        if len(playlist) == 0:
            print("Playlist is empty.")
        else:
            print("\n===== PLAYLIST =====")

            # Display all songs in the playlist
            for index, song in enumerate(playlist, start=1):
                print(f"{index}. {song}")

    elif choice == 3:
        song = input("Enter song name to search: ")

        if song in playlist:
            print("Song is available in the playlist.")
        else:
            print("Song not found.")

    elif choice == 4:
        song = input("Enter song name to remove: ")

        if song in playlist:
            playlist.remove(song)
            print("Song removed successfully.")
        else:
            print("Song not found.")

    elif choice == 5:
        print(f"Total Songs: {len(playlist)}")

    elif choice == 6:
        print("Thank you for using Music Playlist Manager.")
        break

    else:
        print("Invalid choice. Please try again.")
