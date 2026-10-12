''' Bonus 1 - Move Zeros Moves zeros to the beginning '''


numbers = [8,7,-2,0,34,10,0]

zeros = []
non_zeros  = []
for nunmber in numbers:
    if nunmber == 0:
        zeros.append(nunmber)
    else:
        non_zeros.append(nunmber)
result = zeros + non_zeros
print(result)