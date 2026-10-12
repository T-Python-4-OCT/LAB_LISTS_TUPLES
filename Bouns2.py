
def decode_transmission():
    transmission = [
        [18, 0, 19, 8, -2, 17],
        [99, 23, 11, 8],
        [10, 4, 55, 23, 8],
    ]

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

   
    cleaned = list(map(
        lambda word: list(filter(lambda num: 4 <= num <= 29, word)),
        transmission
    ))

    print("Cleaned transmission:")
    print(cleaned)

    
    decoded_words = list(map(lambda word: "".join(map(lambda num: alphabet[num - 4], word)),
        cleaned
    ))

    print("\nDecoded words:")
    print(decoded_words)

    
    secret_message = " ".join(decoded_words)

    print("\nSecret message:")
    print(secret_message)

    
    corrupted_values = list(map(
        lambda original, clean: len(original) - len(clean),
        transmission,
        cleaned
    ))

    print("\nCorrupted values per word:")
    print(corrupted_values)

    
    total_noise = sum(corrupted_values)

    print("Total noise removed:", total_noise)


decode_transmission()
