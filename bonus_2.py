
def clean_transmission(transmission):
    """Remove corrupted numbers while preserving word grouping."""
    return [
        [number for number in word if 4 <= number <= 29]
        for word in transmission
    ]


def decode_words(cleaned_transmission, alphabet):
    """Decode valid numbers into words."""
    return [
        "".join(alphabet[number - 4] for number in word)
        for word in cleaned_transmission
    ]


def reveal_message(decoded_words):
    """Combine decoded words into a single sentence."""
    return " ".join(decoded_words)


def count_corrupted_values(transmission, cleaned_transmission):
    """Count corrupted values in each original word."""
    return [
        len(word) - len(cleaned_word)
        for word, cleaned_word in zip(transmission, cleaned_transmission)
    ]


def main():
    """Run the transmission decoding program."""
    transmission = [
       [9, 12, -5, 17, 7],
    [14, 0, 8, 28, 100]
    ]

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cleaned_transmission = clean_transmission(transmission)


    decoded_words = decode_words(cleaned_transmission, alphabet)

    secret_message = reveal_message(decoded_words)

    corrupted_values = count_corrupted_values(transmission, cleaned_transmission )

    print("Cleaned transmission:")
    print(cleaned_transmission)

    print("\nDecoded words:")
    print(decoded_words)

    print("\nSecret message:")
    print(secret_message)

    print("\nCorrupted values per word:")
    print(corrupted_values)


if __name__ == "__main__":
    main()
