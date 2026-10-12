numbers = [8, 7, -2, 0, 34, 10, 0]

sorted_numbers = sorted(numbers, key=lambda x: (x != 0, x))

print(sorted_numbers)