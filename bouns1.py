numbers = [8, 7, -2, 0, 34, 10, 0]

# استخراج الأصفار وحدها، وجمعها مع باقي الأرقام
sorted_numbers = [n for n in numbers if n == 0] + [n for n in numbers if n != 0]

print(sorted_numbers)