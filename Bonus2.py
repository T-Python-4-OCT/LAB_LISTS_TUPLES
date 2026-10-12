def decode_signal(transmission):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    cleaned_transmission = [[num for num in word if 4 <= num <= 29] for word in transmission]
    print("Cleaned transmission:\n", cleaned_transmission)

    decoded_words = ["".join([alphabet[num - 4] for num in word]) for word in cleaned_transmission]
    print("\nDecoded words:\n", decoded_words)

    secret_message = " ".join(decoded_words)
    print("\nSecret message:\n", secret_message)

    corrupted_values = [len([num for num in word if num < 4 or num > 29]) for word in transmission]
    print("\nCorrupted values per word:\n", corrupted_values)



print("--- Original Mission ---")
transmission_1 = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

decode_signal(transmission_1)



print("\n\n--- Challenge Mission ---")
transmission_2 = [
    [9, 12, -5, 17, 7],
    [14, 0, 8, 28, 100]
]
decode_signal(transmission_2)