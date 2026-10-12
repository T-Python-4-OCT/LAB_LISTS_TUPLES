

movies_rev = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1]),
]
 
good_movies = []
 
#يحسب متوسط ويحذف اقل من 6
for title, year, ratings in movies_rev:
    average = sum(ratings) / len(ratings)
    if average >= 6.0:
        good_movies.append((average, title, year))
 
#يرتب من اعلى للاقل
good_movies.sort(reverse=True)
 
#عرض
number = 1
for average, title, year in good_movies:
    print(f"{number}. {title} ({year}) - Average rating: {average:.2f}")
    number += 1

print()


 #اضافه بسيطه مني
best_average, best_title, best_year = good_movies[0]
print(f"Best movie: {best_title} ({best_year}) - {best_average:.2f}")


removed_count = len(movies_rev) - len(good_movies)
print(f"Movies removed: {removed_count}")


#MohammedAlnsafi
