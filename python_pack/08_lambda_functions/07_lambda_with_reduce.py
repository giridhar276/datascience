from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda first, second: first * second, numbers)
maximum = reduce(lambda first, second: first if first > second else second, numbers)

print(product)
print(maximum)
