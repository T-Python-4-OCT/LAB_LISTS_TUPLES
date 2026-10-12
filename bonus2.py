# Bonus 2

transmission_lists = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cleaned = [[n for n in word if 4 <= n <= 29]
           for word in transmission_lists]

decoded = [
    ''.join([alphabet[n - 4] for n in word])
    for word in cleaned
]

Secret_message = ' '.join(decoded)

corrupted = [
    len([n for n in word if n < 4 or n > 29])
    for word in transmission_lists
]

print("Cleaned transmission:")
print(cleaned)

print("\nDecoded words:")
print(decoded)

print("\nSecret message:")
print(Secret_message)

print("\nCorrupted values per word:")
print(corrupted)