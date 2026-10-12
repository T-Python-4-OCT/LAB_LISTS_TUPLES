movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
def get_movie_ratings(movies_list):
    """
    Calculate each movie's average score and filter out ratings below 6.0.
    """
    movie_ratings = []
    for title, year, ratings in movies_list:
        average = sum(ratings) / len(ratings)
        if average >= 6.0:
            movie_ratings.append((title, year, average))
    return movie_ratings


def sort_ratings(movie_ratings):
    """
    Sort the filtered movies in descending order based on average rating.
    """
    movie_ratings.sort(key=lambda movie: movie[2], reverse=True)
    return movie_ratings


def print_movie_ratings(movie_ratings):
    """
    Display ranked movies with formatted titles, release years, and average scores.
    """
    for index, (title, year, average) in enumerate(movie_ratings, start=1):
        print(f"{index}. {title} ({year}) - Average rating: {average:.2f} ★")

ratings = get_movie_ratings(movies)
sorted_ratings = sort_ratings(ratings)
print_movie_ratings(sorted_ratings)