

numbers = [8, 7, -2, 0, 34, 10, 0]


new_list = []
for number in numbers:
    if number == 0:
        new_list.insert(0, number)
    else:
        new_list.append(number)

print(new_list)










