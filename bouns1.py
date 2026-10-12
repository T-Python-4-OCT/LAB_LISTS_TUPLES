numbers = [8, 7, -2, 0, 34, 10, 0]
result = [x for x in numbers if x == 0] + [x for x in numbers if x != 0]
print(result)
        