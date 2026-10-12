alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# First transmission
transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

cleaned_transmission = [
    [number for number in word if number >= 4 and number <= 29]
    for word in transmission
]

decoded_words = [
    "".join([alphabet[number - 4] for number in word])
    for word in cleaned_transmission
]

message = " ".join(decoded_words)

corrupted_values = [
    len([number for number in word if number < 4 or number > 29])
    for word in transmission
]

print("Cleaned transmission:")
print(cleaned_transmission)

print("Decoded words:")
print(decoded_words)

print("Secret message:")
print(message)

print("Corrupted values per word:")
print(corrupted_values)


# Challenge transmission
transmission = [
    [9, 12, -5, 17, 7],
    [14, 0, 8, 28, 100]
]

cleaned_transmission = [
    [number for number in word if number >= 4 and number <= 29]
    for word in transmission
]

decoded_words = [
    "".join([alphabet[number - 4] for number in word])
    for word in cleaned_transmission
]

message = " ".join(decoded_words)

corrupted_values = [
    len([number for number in word if number < 4 or number > 29])
    for word in transmission
]

print()
print("Challenge:")
print("Cleaned transmission:")
print(cleaned_transmission)

print("Decoded words:")
print(decoded_words)

print("Secret message:")
print(message)

print("Corrupted values per word:")
print(corrupted_values)