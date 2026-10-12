''' Decode a Message Cleans and decodes the transmission '''


transmission = [
    [9,12,-5,17,7],
    [14,0,8,28,100]
    ]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cleaned = [
    [x for x in word if 4 <= x <= 29]
    for word in transmission
]

print("cleaned transmission")
print(cleaned)
decoded_words =[
    "".join(alphabet[x - 4 ] for x in word)
    for word in cleaned
   ]
print("Decoded_words")
print(decoded_words)
message = " ".join(decoded_words)
print("Secret message 🔐")
print(message)
corrupted = [
    len([x for x in word if x <4 or x >29])
    for word in transmission
]
print("corrupted values per word:")
print (corrupted)
print("Decryption complete ✅ ")