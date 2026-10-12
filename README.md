# LAB_LISTS_TUPLES

## Movie Ratings Analysis

Scenario:
You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
2. Calculates the average rating for each movie.
3. Filters out movies with an average rating lower than 6.0.
5. Displays the  movies, along with their title, release year, and average rating.

Example input:
```
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
```

Expected output:
```
1. The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★
```


## Bonus 1
Using the following list, we need a program that will arrange the list so the zeros are at the beginning.
```
numbers = [8, 7, -2, 0, 34, 10, 0]

```

## Bonus 2

### Mission: Decode a Message

A  station has received a mysterious transmission from an unknown source. Unfortunately, the signal was corrupted, and random numbers were mixed into the message.

Your mission is to recover the original message using Python list comprehensions.

### The Data

The transmission consists of several lists of numbers. Each inner list represents one word.

```
transmission = [    [18, 0, 19, 8, -2, 17],    [99, 23, 11, 8],    [10, 4, 55, 23, 8]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

### Decoding Rules

1. Each number represents a letter of the English alphabet.
2. The letters have been encrypted by adding 3 to their alphabetical position.
3. Therefore, `4 = A`, `5 = B`, `6 = C`, ..., `29 = Z`.
4. Any number outside the range 4–29 is corrupted data and must be ignored.
5. Each inner list represents a separate word.

For example:

```
Encrypted:  [11, 8, 15, 15, 18]
Decoded:    H E L L O
Result:     HELLO
```

### Your Tasks

Task 1 — Remove the Noise

Use list comprehension to create a new nested list containing only valid numbers (4–29), while preserving the original grouping.

Task 2 — Decode the Words

Task 3 — Reveal the Message (Combine the decoded words into a single sentence with spaces between them).

Task 4 — Signal Diagnostics

Create a list containing the number of corrupted values found in each original inner list. Use list comprehension for this task too.

### Expected Output

```
Cleaned transmission:
[[18, 19, 8, 17], [23, 11, 8], [10, 4, 23, 8]]

Decoded words:
['OPEN', 'THE', 'GATE']

Secret message:
OPEN THE GATE

Corrupted values per word:
[2, 1, 1]
```

### Requirements

- Use list comprehensions for filtering and transforming data.
- Do not use regular `for` or `while` loops.
- Do not hardcode the decoded message.
- You may use string indexing, `.join()`, `len()`, and other basic Python operations.
- Your program must work with other transmissions following the same rules.

### Challenge

You receives another transmission:

```
transmission = [    [9, 12, -5, 17, 7],    [14, 0, 8, 28, 100]]
```

Your existing program should decode this transmission correctly without modifying the decoding logic.
