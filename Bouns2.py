transmission = [
    [9, 12, -5, 17, 7],
    [14, 0, 8, 28, 100]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


cleaned = [
    [number for number in word if 4 <= number <= 29]
    for word in transmission
]


decoded_words = [
    "".join([alphabet[number - 4] for number in word])
    for word in cleaned
]



secret_message = " ".join(decoded_words)


corrupted = [
    len(word) - len([number for number in word if 4 <= number <= 29])
    for word in transmission
]


print("Cleaned transmission:")
print(cleaned)

print("Decoded words:")
print(decoded_words)

print("Secret message:")
print(secret_message)

print("Corrupted values per word:")
print(corrupted)
