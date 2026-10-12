movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1]),
    ("Nasser Almuzaini", 2004, [10, 10, 10, 10, 10, 10])
]

def calculate_average_rating(ratings):
    if not ratings:
        return 0
    return sum(ratings) / len(ratings) 

class Movie:
    def __init__(self, title, year, ratings):
        self.title = title
        self.year = year
        self.ratings = ratings
        self.average_rating = calculate_average_rating(ratings)
        
    def __str__(self):
        return f"{self.title} ({self.year}) - Average Rating: {self.average_rating:.2f} ★"

def main():
    
    movie_objects = []
    
    
    for item in movies:
        title = item[0]     
        year = item[1]      
        ratings = item[2]   
        

        my_movie = Movie(title, year, ratings)
        

        movie_objects.append(my_movie)


    for movie in movie_objects:
        if movie.average_rating >= 6:
            print(movie)

if __name__ == "__main__":
    main()

