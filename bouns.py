
numbers = [8, 7, -2, 0, 34, 10, 0]


result = sorted(numbers, key=lambda x: (x != 0, x))

print(result)