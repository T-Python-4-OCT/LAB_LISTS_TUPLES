alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Main Transmission
transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

cleaned_transmission = [[num for num in word if 4 <= num <= 29] for word in transmission]

decoded_words = ["".join([alphabet[num - 4] for num in word]) for word in cleaned_transmission]

secret_message = " ".join(decoded_words)

corrupted_counts = [len([num for num in word if not (4 <= num <= 29)]) for word in transmission]

print("Cleaned transmission:")
print(cleaned_transmission)

print("\nDecoded words:")
print(decoded_words)

print("\nSecret message:")
print(secret_message)

print("\nCorrupted values per word:")
print(corrupted_counts)



# Challenge Solution
# ==========================================
# transmission = [
#     [9, 12, -5, 17, 7],
#     [14, 0, 8, 28, 100]
# ]

# Expected Output for Challenge:
# Cleaned transmission: [[9, 12, 17, 7], [14, 8, 28]]
# Decoded words: ['FIND', 'KEY']
# Secret message: FIND KEY
# Corrupted values per word: [1, 2]