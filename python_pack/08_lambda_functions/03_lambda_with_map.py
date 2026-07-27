numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda number: number ** 2, numbers))
fahrenheit = list(map(lambda celsius: (celsius * 9 / 5) + 32, [0, 20, 30, 40]))

print(squares)
print(fahrenheit)
