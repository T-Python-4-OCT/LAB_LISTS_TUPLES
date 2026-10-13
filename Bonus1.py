Numbers = [8, 7, -2, 0, 34, 10, 0]
Zeros = []
NonZeros = []
for number in Numbers :
  if number == 0 :
    Zeros.append(number)
  else :
    NonZeros.append(number)

Zeros.extend(NonZeros)
print(Zeros)    
