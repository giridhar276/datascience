def calculate_sum(*numbers):
    print("Received tuple:", numbers)
    return sum(numbers)

print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30, 40))
