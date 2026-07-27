numbers = list(range(1, 11))
result = list(
    map(
        lambda number: number ** 2,
        filter(lambda number: number % 2 == 0, numbers),
    )
)
print(result)
