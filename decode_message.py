
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decode(transmission):
    cleaned = []          
    decoded_words = []    
    corrupted = []        

    for word in transmission:
        clean_word = []
        bad_count = 0

        for n in word:
            if n >= 4 and n <= 29:
                clean_word.append(n)
            else:
                bad_count = bad_count + 1

        cleaned.append(clean_word)
        corrupted.append(bad_count)

        letters = ""
        for n in clean_word:
            letters = letters + alphabet[n - 4]
        decoded_words.append(letters)

    message = ""
    for i in range(len(decoded_words)):
        if i > 0:
            message = message + " "
        message = message + decoded_words[i]

    return cleaned, decoded_words, message, corrupted


def show(transmission):
    cleaned, decoded_words, message, corrupted = decode(transmission)
    print("Cleaned transmission:")
    print(cleaned)
    print("\nDecoded words:")
    print(decoded_words)
    print("\nSecret message:")
    print(message)
    print("\nCorrupted values per word:")
    print(corrupted)


transmission = [[18, 0, 19, 8, -2, 17], [99, 23, 11, 8], [10, 4, 55, 23, 8]]
show(transmission)

print("\n" + "=" * 30 + " CHALLENGE " + "=" * 30 + "\n")
transmission2 = [[9, 12, -5, 17, 7], [14, 0, 8, 28, 100]]
show(transmission2)