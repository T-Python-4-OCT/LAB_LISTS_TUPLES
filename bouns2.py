
transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Remove the noise
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

# Task 4: Count corrupted values
corrupted_counts = [
    len(word) - len(clean_word)
    for word, clean_word in zip(transmission, cleaned)
]

print("\nCorrupted values per word:")
print(corrupted_counts)
