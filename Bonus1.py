numbers = [8, 7, -2, 0, 34, 10, 0]

zeros = []
other_numbers = []

for number in numbers:
    if number == 0:
        zeros.append(number)
    else:
        other_numbers.append(number)

numbers = zeros + other_numbers

print(numbers)