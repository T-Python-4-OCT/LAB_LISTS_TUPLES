transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


cleaned_transmission = [[num for num in inner_list if 4 <= num <= 29] for inner_list in transmission]


decoded_words = ["".join([alphabet[num - 4] for num in inner_list]) for inner_list in cleaned_transmission]


secret_message = " ".join(decoded_words)


corrupted_values = [len([num for num in inner_list if not (4 <= num <= 29)]) for inner_list in transmission]


print("Cleaned transmission:")
print(cleaned_transmission)

print("\nDecoded words:")
print(decoded_words)

print("\nSecret message:")
print(secret_message)

print("\nCorrupted values per word:")
print(corrupted_values)