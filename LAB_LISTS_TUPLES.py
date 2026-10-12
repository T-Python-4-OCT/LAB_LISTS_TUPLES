movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


def show_movies(movies):
    movie_results = []

    for movie in movies:
        title = movie[0]
        year = movie[1]
        ratings = movie[2]
        average = sum(ratings) / len(ratings)

        if average >= 6:
            movie_results.append((title, year, average))

    movie_results.sort(key=lambda movie: movie[2], reverse=True)

    for index, movie in enumerate(movie_results, start=1):
        title = movie[0]
        year = movie[1]
        average = movie[2]
        print(f"{index}. {title} ({year}) - Average rating: {average:.2f} ")


show_movies(movies)


