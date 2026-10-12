numbers = [8, 7, -2, 0, 34, 10, 0]

zer=[]
num=[]

for x in numbers: # create loop to filter zeros from another digit  
    if x == 0:
        zer.append(x)
    else:
        num.append(x)

total_a=zer+num # add zero list to another number list
print(total_a)