numbers = [8, 7, -2, 0, 34, 10, 0]

zeros = []
others = []

for number in numbers:
    if number == 0:
        zeros.append(number)
    else:
        others.append(number)

numbers = zeros + others
print(numbers)

#MohammedAlnsafi