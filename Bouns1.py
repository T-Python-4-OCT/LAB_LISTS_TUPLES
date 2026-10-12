numbers = [8, 7, -2, 0, 34, 10, 0]

new_numbers = []

for number in numbers:
    if number == 0:
        new_numbers.insert(0, number)
    else:
        new_numbers.append(number)

print(new_numbers)