numbers = list(range(1, 21))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
above_ten = list(filter(lambda number: number > 10, numbers))

print(even_numbers)
print(above_ten)
