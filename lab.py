movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


approved_films = []

for film in movies:

    film_name = film[0]
    film_year = film[1]
    film_scores = film[2]
    

    avg_score = sum(film_scores) / len(film_scores)
    

    if avg_score >= 6.0:

        approved_films.append([film_name, film_year, avg_score])


def sort_by_avg(item):
    return item[2]

approved_films.sort(key=sort_by_avg, reverse=True)


rank = 1
for f in approved_films:
    print(f"{rank}. {f[0]} ({f[1]}) - Average rating: {f[2]:.2f} ★")
    rank += 1