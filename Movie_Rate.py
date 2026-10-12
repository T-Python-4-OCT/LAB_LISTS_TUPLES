movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

#For calculating the average rating 
rated_movies = [
    (title, year, sum(ratings) / len(ratings))
    for title, year, ratings in movies
    if ratings and sum(ratings) / len(ratings) > 6.0
]

rated_movies.sort(key=lambda movie: movie[2], reverse=True)

for number, (title, year, average) in enumerate(rated_movies, start=1):
    print(f"{number}. {title} ({year}) - Average rating: {average:.2f} ★")
