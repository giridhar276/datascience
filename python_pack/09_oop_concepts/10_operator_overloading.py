class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

first = Vector(2, 3)
second = Vector(4, 5)
print(first + second)
