# Bonus 1
numbers = [8, 7, -2, 0, 34, 10, 0]

sorted_list = sorted(numbers, key=lambda i: (i != 0, i))

print(sorted_list)