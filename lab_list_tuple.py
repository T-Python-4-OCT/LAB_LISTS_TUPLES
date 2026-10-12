movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

qualified_movies = []

for movie in movies:
    title = movie[0]
    year = movie[1]
    ratings = movie[2]

    average_rating = sum(ratings) / len(ratings)

    if average_rating >= 6.0:
        qualified_movies.append((title, year, average_rating))

qualified_movies.sort(key=lambda movie: movie[2], reverse=True)

for index, movie in enumerate(qualified_movies, start=1):
    title, year, average_rating = movie

    print(f"{index}. {title} ({year}) - "  f"Average rating: {average_rating:.2f} ★" )
