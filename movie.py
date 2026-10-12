movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
results = []
for movie in movies:
    title = movie[0]
    year = movie[1]
    ratings = movie[2]

    average = sum(ratings) / len(ratings)

    if average >= 6.0:
        results.append((average, title, year))


    results.sort(reverse=True)
    number = 1
    for result in results:
        average = result[0]
        title = result[1]
        year = result[2]
        print(f"{number}. {title} ({year}) - Average Rating: {average:.2f}*")
        print("_" *50)
        number += 1