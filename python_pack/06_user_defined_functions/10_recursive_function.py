def factorial(number):
    if number < 0:
        raise ValueError("Number must be non-negative")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)

print(factorial(5))
