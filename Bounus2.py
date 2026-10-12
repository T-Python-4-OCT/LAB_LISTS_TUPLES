transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Task 1: Remove the Noise
cleaned_transmission = [
    [num for num in word if 4 <= num <= 29]
    for word in transmission
]

print("Cleaned transmission:")
print(cleaned_transmission)

# Task 2: Decode the Words
decoded_word = [
    "".join(alphabet[num - 4] for num in word)
    for word in cleaned_transmission
]

print("\nDecoded word:")
print(decoded_word)

# Task 3: Reveal the Message
secret_message = " ".join(decoded_word)

print("\nSecret message:")
print(secret_message)

# Task 4: Signal Diagnostics
corrupted_values = [
    len(word) - len(cleaned_word)
    for word, cleaned_word in zip(transmission, cleaned_transmission)
]

print("\nCorrupted values per word:")
print(corrupted_values)