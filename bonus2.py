alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SHIFT = 3


def decode(transmission):
    cleaned = [[number for number in word if 4 <= number <= 29] for word in transmission]

    words = ["".join([alphabet[number - SHIFT - 1] for number in word]) for word in cleaned]

    message = " ".join(words)

    corrupted = [len(transmission[i]) - len(cleaned[i]) for i in range(len(transmission))]

    print("Cleaned transmission:")
    print(cleaned)
    print()
    print("Decoded words:")
    print(words)
    print()
    print("Secret message:")
    print(message)
    print()
    print("Corrupted values per word:")
    print(corrupted)


transmission = [[18, 0, 19, 8, -2, 17], [99, 23, 11, 8], [10, 4, 55, 23, 8]]
decode(transmission)

print()
print("----- Challenge -----")
print()

transmission = [[9, 12, -5, 17, 7], [14, 0, 8, 28, 100]]
decode(transmission)
