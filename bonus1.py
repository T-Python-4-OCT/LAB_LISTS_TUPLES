numbers = [8, 7, -2, 0, 34, 10, 0]
numbers.sort(key=lambda number: (number != 0, number))

print(numbers)