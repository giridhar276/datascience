squares = [number ** 2 for number in range(1, 6)]
even_squares = [number ** 2 for number in range(1, 11) if number % 2 == 0]
word_lengths = {word: len(word) for word in ["Python", "Pandas", "Flask"]}
unique_remainders = {number % 3 for number in range(10)}

print(squares)
print(even_squares)
print(word_lengths)
print(unique_remainders)
