transmission = [    [9, 12, -5, 17, 7],    [14, 0, 8, 28, 100]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

code = {i + 4: letter for i, letter in enumerate(alphabet)}

cleaned = [[n for n in word if n in code] for word in transmission]

decoded_words = ["".join([code[n] for n in word]) for word in cleaned]

message = " ".join(decoded_words)


corrupted = [len([n for n in word if n not in code]) for word in transmission]

print("Cleaned transmission:")
print(cleaned)
print("\nDecoded words:")
print(decoded_words)
print("\nSecret message:")
print(message)
print("\nCorrupted values per word:")
print(corrupted)