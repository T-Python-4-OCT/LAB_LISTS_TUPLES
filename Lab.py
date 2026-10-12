
Movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

RatedMovies = []

for movie in Movies:
    Title = movie[0]
    Year = movie[1] 
    Ratings = movie[2]
    Average = sum(Ratings) / len(Ratings)

    if Average >= 6.0:
        RatedMovies.append((Title, Year, round(Average, 2)))

while len(RatedMovies) > 0:
    Averages = []

    for movie in RatedMovies:
        Averages.append(movie[2])

    Highest = max(Averages)

    for movie in RatedMovies:
        if movie[2] == Highest:
            print(movie[0], movie[1], "-", "Average Rating:", movie[2])
            RatedMovies.remove(movie)
            break