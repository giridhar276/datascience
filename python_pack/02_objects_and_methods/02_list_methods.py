"""All commonly used list methods."""

numbers = [30, 10, 20, 10]
print("Original:", numbers)

numbers.append(40)
print("append:", numbers)

numbers.extend([50, 60])
print("extend:", numbers)

numbers.insert(1, 15)
print("insert:", numbers)

numbers.remove(10)
print("remove first 10:", numbers)

removed = numbers.pop()
print("pop value:", removed, "remaining:", numbers)

print("index of 20:", numbers.index(20))
print("count of 10:", numbers.count(10))

numbers.sort()
print("sort ascending:", numbers)

numbers.reverse()
print("reverse:", numbers)

copied = numbers.copy()
print("copy:", copied)

copied.clear()
print("clear copied list:", copied)
