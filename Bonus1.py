numbers = [8, 7, -2, 0, 34, 10, 0]
print(f"Original list: {numbers}")
count = 0
while 0 in numbers:
    numbers.remove(0)
    count += 1
print(f"List after removing zeros: {numbers}")
while count > 0:
    numbers.insert(0, 0)
    count -= 1
print(f"List with zeros at the beginning: {numbers}")