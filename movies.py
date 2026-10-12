def calculate_average(ratings):
    total = 0
    for rating in ratings:
        total += rating
    return total / len(ratings)

def add_avarage(movies):
    result = []
    for title,year,ratings in movies:
        result.append((title, year, ratings, calculate_average(ratings)))
    return result

def fliter_movies(movies_with_avg,min_avg):
    result =[]
    for movie in movies_with_avg:
        if movie[3] >= min_avg:
            result.append(movie)
    return result

def get_movies(movie):
    return movie[3]

def sort_movies(movies_with_avg):
    return sorted(movies_with_avg,key=get_movies,reverse=True)

def display_movies(movies_with_avg):
    for num,(title,year,ratings,avg) in enumerate(movies_with_avg):
        print(f"{num+1}. {title} ({year}) - Average Rating: {avg:.2f}")

def main():
    movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1]),
]
    movies_with_avg = add_avarage(movies)
    filtered_movies = fliter_movies(movies_with_avg, 6.0)
    sorted_movies = sort_movies(filtered_movies)
    display_movies(sorted_movies)

main()























