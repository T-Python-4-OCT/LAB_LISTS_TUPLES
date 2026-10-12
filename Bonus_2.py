transmission = [    [9, 12, -5, 17, 7],    [14, 0, 8, 28, 100]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cleaned_transmission = [[n for n in word if 4 <= n <= 29] for word in transmission]
print("Cleaned transmission:")
print(cleaned_transmission)

decoded_words = ["".join([alphabet[n - 4] for n in word]) for word in cleaned_transmission]
print("\nDecoded words:")
print(decoded_words)

secret_message = " ".join(decoded_words)
print("\nSecret message:")
print(secret_message)

corrupted_counts = [len(word) - len(cleaned) for word, cleaned in zip(transmission, cleaned_transmission)]
print("\nCorrupted values per word:")
print(corrupted_counts)