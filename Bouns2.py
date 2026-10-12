transmission = [   [18, 0, 19, 8, -2, 17],    [99, 23, 11, 8],    [10, 4, 55, 23, 8],]

#transmission = [[9, 12, -5, 17, 7], [14, 0, 8, 28, 100]]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 

cleaned = [[n for n in word if 4 <= n <= 29] for word in transmission]
 

decoded_words = ["".join([alphabet[n - 4] for n in word]) for word in cleaned]

 
secret_message = " ".join(decoded_words)
 

corrupted_counts = [len([n for n in word if not 4 <= n <= 29]) for word in transmission]
 
print("Cleaned transmission:")
print(cleaned)
print()
print("Decoded words:")
print(decoded_words)
print()
print("Secret message:")
print(secret_message)
print()
print("Corrupted values per word:")
print(corrupted_counts)


 #MohammedAlnsafi