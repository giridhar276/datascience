"""Converting values from one object type to another."""

text_number = "250"
number = int(text_number)
price = float("45.75")
items = tuple(["A", "B", "C"])
unique_items = set([1, 1, 2, 3])
characters = list("Python")

print(number, type(number))
print(price, type(price))
print(items, type(items))
print(unique_items, type(unique_items))
print(characters, type(characters))
