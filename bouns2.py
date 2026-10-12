transmission = [    [9, 12, -5, 17, 7],    [14, 0, 8, 28, 100]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cleaned = []
decoded_words = []
corrupted = []

for word in transmission:
    clean_word = []  
    letters = ""  
    bad_count = 0  

    for n in word:
        if 4 <= n <= 29:
            clean_word.append(n)
            letters += alphabet[n - 4]
        else:
            bad_count += 1

    cleaned.append(clean_word)
    decoded_words.append(letters)
    corrupted.append(bad_count)

message = " ".join(decoded_words)

print("Cleaned transmission:")
print(cleaned)
print("\nDecoded words:")
print(decoded_words)
print("\nSecret message:")
print(message)
print("\nCorrupted values per word:")
print(corrupted)