transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

def decode_transmission(transmission):
    """Filters out noise and decodes the message."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    cleaned = [[n for n in word if 4 <= n <= 29] for word in transmission]
    words = ["".join(alphabet[n - 4] for n in word) for word in cleaned]
    message = " ".join(words)
    corrupted = [len([n for n in word if n < 4 or n > 29]) for word in transmission]
    
    return cleaned, words, message, corrupted



cleaned, words, message, corrupted = decode_transmission(transmission)

print("Cleaned transmission:")
print(cleaned)
print("\nDecoded words:")
print(words)
print("\nSecret message:")
print(message)
print("\nCorrupted values per word:")
print(corrupted)

challenge = [
    [9, 12, -5, 17, 7],
    [14, 0, 8, 28, 100]
]

_, _, challenge_message, _ = decode_transmission(challenge)
print("\nChallenge decoded message:")
print(challenge_message)

