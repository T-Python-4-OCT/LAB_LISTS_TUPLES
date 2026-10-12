alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decode_transmission(transmission):
    #هنا سوينا داله واضفنا لها كل المنطق حق التشفير السبب هو عشان نقدر نستخدمها على اكثر من ترانزميشن
    cleaned_transmission = [[num for num in word if 4 <= num <= 29] for word in transmission]
    decoded_words = ["".join([alphabet[num - 4] for num in word]) for word in cleaned_transmission]
    secret_message = " ".join(decoded_words)
    corrupted_counts = [len([num for num in word if not (4 <= num <= 29)]) for word in transmission]
    
    print("Cleaned transmission:", cleaned_transmission)
    print("Decoded words:", decoded_words)
    print("Secret message:", secret_message)
    print("Corrupted values per word:", corrupted_counts)
    print("-" * 40)

transmission_1 = [
    [18, 0, 19, 8, -2, 17], 
    [99, 23, 11, 8], 
    [10, 4, 55, 23, 8]
]

print("=== Transmission 1 Result ===")
decode_transmission(transmission_1)

transmission_2 = [
    [9, 12, -5, 17, 7], 
    [14, 0, 8, 28, 100]
]

print("\n=== Transmission 2 (Challenge) Result ===")
decode_transmission(transmission_2)