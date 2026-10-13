transmission = [    [18, 0, 19, 8, -2, 17],    [99, 23, 11, 8],    [10, 4, 55, 23, 8]]
transmission2 = [    [9, 12, -5, 17, 7],    [14, 0, 8, 28, 100]]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def remove_corrupted_data(transmission_list):
    return [
        [num for num in row if 4 <= num <= 29]
        for row in transmission_list
    ]


def decode_words(cleaned_list):
    return [
        "".join([alphabet[num - 4] for num in row])
        for row in cleaned_list
    ]


def count_corrupted_values(transmission_list):
    return [
        len([num for num in row if num < 4 or num > 29])
        for row in transmission_list
    ]


def run(transmission_list):
    cleaned_data = remove_corrupted_data(transmission_list)
    decoded_words = decode_words(cleaned_data)
    secret_message = " ".join(decoded_words)
    corrupted_counts = count_corrupted_values(transmission_list)

    print("Cleaned transmission:")
    print(cleaned_data)

    print("\nDecoded words:")
    print(decoded_words)

    print("\nSecret message:")
    print(secret_message)

    print("\nCorrupted values per word:")
    print(corrupted_counts)


run(transmission)
run(transmission2)