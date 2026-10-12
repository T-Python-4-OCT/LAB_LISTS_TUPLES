movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

best_movies = []

for movie in movies:
    title, year, ratings = movie          
    average = sum(ratings) / len(ratings)
      # remove movies lower than 6.0
    if average >= 6.0:                     
        best_movies.append((title, year, average))


def get_average(item):
    return item[2]


best_movies.sort(key=get_average, reverse=True)   # highest rating first ok 

number = 1
for movie in best_movies:
    print(f"{number}. {movie[0]} ({movie[1]}) - Average rate: {movie[2]:.2f} ★")
    number = number + 1