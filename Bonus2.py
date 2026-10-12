alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decode_transmission(transmission):

    # Task 1
    cleaned = [[num for num in word if 4 <= num <= 29] for word in transmission]
    print("Cleaned transmission:")
    print(cleaned)


    # Task 2  
    words = ["".join([alphabet[num - 4] for num in word]) for word in cleaned]
    print("\nDecoded words:")
    print(words)


    # Task 3
    message = " ".join(words)
    print("\nSecret message:")
    print(message)
    

    # Task 4
    bad_counts = [len([num for num in word if num < 4 or num > 29]) for word in transmission]
    print("\nCorrupted values per word:")
    print(bad_counts)


transmission = [[18, 0, 19, 8, -2, 17], [99, 23, 11, 8], [10, 4, 55, 23, 8]]
decode_transmission(transmission)



print("\n-------------- Challenge ---------------\n")
new_transmission = [[9, 12, -5, 17, 7], [14, 0, 8, 28, 100]]
decode_transmission(new_transmission)




# -------------- Output ---------------
# Cleaned transmission:
# [[18, 19, 8, 17], [23, 11, 8], [10, 4, 23, 8]]

# Decoded words:
# ['OPEN', 'THE', 'GATE']

# Secret message:
# OPEN THE GATE

# Corrupted values per word:
# [2, 1, 1]

# -------------- Challenge ---------------

# Cleaned transmission:
# [[9, 12, 17, 7], [14, 8, 28]]

# Decoded words:
# ['FIND', 'KEY']

# Secret message:
# FIND KEY

# Corrupted values per word:
# [1, 2]
