transmission = [
    [9, 12, -5, 17, 7],
    [14, 0, 8, 28, 100]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cleaned = [[n for n in word if 4 <= n <= 29] for word in transmission]
words = ["".join([alphabet[n - 4] for n in word]) for word in cleaned]
corrupted = [len([n for n in word if n < 4 or n > 29]) for word in transmission]

print("Cleaned transmission:", cleaned)
print("Decoded words:", words)
print("Secret message:", " ".join(words))
print("Corrupted values per word:", corrupted)
