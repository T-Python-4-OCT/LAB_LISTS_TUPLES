transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

transmission_two = [    [9, 12, -5, 17, 7],    [14, 0, 8, 28, 100]]


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decode_transmission(transmission, low=4, high=29):
    is_valid = lambda n: low <= n <= high

    cleaned = list(map(lambda word: list(filter(is_valid, word)), transmission))
    decoded = list(map(lambda word: "".join(map(lambda n: alphabet[n - low], word)), cleaned))
    message = " ".join(decoded)
    corrupted = list(map(lambda w, c: len(w) - len(c), transmission, cleaned))

    return cleaned, decoded, message, corrupted


def show(name, t):
    cleaned, decoded, message, corrupted = decode_transmission(t)

    print(f"===== {name} =====")
    print("Cleaned transmission:")
    print(cleaned)
    print("")
    print("Decoded words:")
    print(decoded)
    print("")
    print("Secret message:")
    print(message)
    print("")
    print("Corrupted values per word:")
    print(corrupted)
    print("")


show("transmission", transmission)
show("transmission_two", transmission_two)