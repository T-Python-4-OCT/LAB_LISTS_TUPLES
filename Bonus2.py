transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Remove the Noise (0 and -2)
Cleaned = [
    [number for number in word if 4 <= number <= 29]
    for word in transmission
]

print("Cleaned transmission:")
print(Cleaned)

# Decode the Words
Decoded = [
    [alphabet[number - 4] for number in word]
    for word in Cleaned ]

DecodedWords = [
    ''.join(word)
    for word in Decoded ]

print()
print("Decoded words:")
print(DecodedWords)

# Reveal the Message 
Message = ' '.join(DecodedWords)
print()
print("Secret message:")
print(Message)

# Signal Diagnostics
Corrupted = [
    len(original) - len(clean)
    for original, clean in zip(transmission, Cleaned)
]

print()
print("Corrupted values per word:")
print(Corrupted)