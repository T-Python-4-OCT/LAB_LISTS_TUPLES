def movie_ratings_analysis(movies):

    filtered_movies = []

    for title, year, reatings in movies:
        average = sum(reatings) / len(reatings)
        if average >= 6:
            filtered_movies.append((title, year, average))

    count = 1
    for title, year, avg in filtered_movies:
        print(f'{count}. {title} ({year}) - Avergae rating: {round(avg, 2)} ★')
        count += 1

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

movie_ratings_analysis(movies)