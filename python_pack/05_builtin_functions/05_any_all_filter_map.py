values = [2, 4, 6, 8]
print("all even:", all(value % 2 == 0 for value in values))
print("any above 5:", any(value > 5 for value in values))
print("map doubled:", list(map(lambda value: value * 2, values)))
print("filter above 4:", list(filter(lambda value: value > 4, values)))
