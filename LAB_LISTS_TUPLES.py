movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

MIN_RATING = 6.0


def average(ratings):
    return sum(ratings) / len(ratings)


# 1. Calculate the average rating for each movie -> (title, year, average)
movie_averages = [(title, year, average(ratings)) for title, year, ratings in movies]

# 2. Filter out movies with an average rating lower than 6.0
good_movies = [movie for movie in movie_averages if movie[2] >= MIN_RATING]

# 3. Sort from highest to lowest average rating
def get_average(movie):
    return movie[2]


good_movies.sort(key=get_average, reverse=True)

# 4. Display the results
for rank, (title, year, avg) in enumerate(good_movies, start=1):
    print(f"{rank}. {title} ({year}) - Average rating: {avg:.2f} ★")
