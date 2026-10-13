
numbers = [8, 7, -2, 0, 34, 10, 0]

zeros = [x for x in numbers if x == 0]
non_zeros = [x for x in numbers if x != 0]

numbers = zeros + non_zeros
print(numbers)