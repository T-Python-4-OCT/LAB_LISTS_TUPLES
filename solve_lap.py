movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


movies_with_avg = []
for title, year, ratings in movies:
    average = sum(ratings) / len(ratings)
    movies_with_avg.append((title, year, average))


filtered = [movie for movie in movies_with_avg if movie[2] >= 6.0]


filtered.sort(key=lambda movie: movie[2], reverse=True)


for i, (title, year, average) in enumerate(filtered, start=1):
    print(f"{i}. {title} ({year}) - Average rating: {average:.2f} ★")