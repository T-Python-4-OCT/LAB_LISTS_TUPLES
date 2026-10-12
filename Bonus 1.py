numbers = [8, 7, -2, 0, 34, 10, 0]

numbers.sort(key=lambda x: 0 if x == 0 else 1)

print(numbers)