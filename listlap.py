movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
def average_cal(x:list):
   #هذي داله اضفناها مهمتها تحسب الافريج او المتوسط الحسابي
   avrege= sum(x[2])/len(x[2])
   
   return (avrege)

def format_print(x):
    #وهذي داله ترتب الناتج وتطبعه بطريقه منسقه ومرتبه
    rsult = "\n".join(
    
        [f"{n[0]} ({n[1]}) - Average rating: {average_cal(n):.2f} ★"
        for n in x
        if average_cal(n) >= 6.0])

    print(rsult)  


format_print(movies)