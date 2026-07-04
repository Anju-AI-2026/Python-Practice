# Program to store and display a movie collection using tuples

movies = []

number_of_movies = int(input("Enter the number of movies: "))

# Store movie details
for i in range(number_of_movies):
    print(f"\nMovie {i + 1}")

    name = input("Enter movie name: ")
    year = int(input("Enter release year: "))
    rating = float(input("Enter movie rating: "))

    movie = (name, year, rating)
    movies.append(movie)

print("\n===== MOVIE COLLECTION =====")

# Display all movie records
for movie in movies:
    print(f"\nMovie Name   : {movie[0]}")
    print(f"Release Year : {movie[1]}")
    print(f"Rating       : {movie[2]}/10")
