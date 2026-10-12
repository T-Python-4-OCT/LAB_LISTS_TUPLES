
transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Task 1: Remove corrupted numbers
cleaned = [
    [n for n in word if 4 <= n <= 29]
    for word in transmission
]

print("Cleaned transmission:")
print(cleaned)

# Task 2: Decode the words
decoded_words = [
    "".join(alphabet[n - 4] for n in word)
    for word in cleaned
]

print("\nDecoded words:")
print(decoded_words)

# Task 3: Reveal the message
message = " ".join(decoded_words)

print("\nSecret message:")
print(message)

# Task 4: Count corrupted numbers in each original word
corrupted = [
    len([n for n in word if n < 4 or n > 29])
    for word in transmission
]

print("\nCorrupted values per word:")
print(corrupted)