numbers = [8, 7, -2, 0, 34, 10, 0]

zeros = [number for number in numbers if number == 0]
others = [number for number in numbers if number != 0]

result = zeros + others

print(result)
