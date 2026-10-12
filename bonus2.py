alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decode_transmission(transmission):
    cleaned = [
        [number for number in word if 4 <= number <= 29]
        for word in transmission
    ]

    decoded_words = [
        "".join([alphabet[number - 4] for number in word])
        for word in cleaned
    ]

    message = " ".join(decoded_words)

    corrupted_counts = [
        len(original) - len(valid)
        for original, valid in zip(transmission, cleaned)
    ]

    print("Cleaned transmission:", cleaned, sep="\n")
    print("Decoded words:", decoded_words, sep="\n")
    print("Secret message:", message, sep="\n")
    print("Corrupted values per word:", corrupted_counts, sep="\n")


transmission1 = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

transmission2 = [
    [9, 12, -5, 17, 7],
    [14, 0, 8, 28, 100]
]

print("Transmission 1 — Original")
decode_transmission(transmission1)

print("\nTransmission 2 — Challenge")
decode_transmission(transmission2)