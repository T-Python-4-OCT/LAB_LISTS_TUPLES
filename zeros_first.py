def zeros_first(numbers):
    zero = []
    other = []
    for num in numbers:
        if num == 0:
            zero.append(num)
        else:
            other.append(num)
    return zero + other

def main():
    numbers = [8, 7, -2, 0, 34, 10, 0]
    print("Original:", numbers)
    print("Arranged:", zeros_first(numbers))

main()