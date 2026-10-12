transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8],
]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cleaned_transmission = [
    [num for num in word if 4 <= num <= 29] for word in transmission
]

decoded_words = [
    "".join([alphabet[num - 4] for num in word]) for word in cleaned_transmission
]

secret_message = " ".join(decoded_words)

corrupted_values_per_word = [
    len(word) - len(cleaned) for word, cleaned in zip(transmission, cleaned_transmission)
]

print(f"Cleaned transmission:\n{cleaned_transmission}")
print(f"\nDecoded words:\n{decoded_words}")
print(f"\nSecret message:\n{secret_message}")
print(f"\nCorrupted values per word:\n{corrupted_values_per_word}")