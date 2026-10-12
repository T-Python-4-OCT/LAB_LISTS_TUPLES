
numbers = [8, 7, -2, 0, 34, 10, 0]

result = [0 for n in numbers if n == 0] + [n for n in numbers if n != 0]

print(result)