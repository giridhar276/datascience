def calculate_discount(amount: float, percentage: float = 10.0) -> float:
    """Return the amount after applying a percentage discount."""
    discount = amount * percentage / 100
    return amount - discount

print(calculate_discount(1000.0, 15.0))
print(calculate_discount.__doc__)
