"""Basic syntax for Python numeric objects: int, float and complex."""

integer_value = 25
float_value = 19.75
complex_value = 3 + 4j

print("Integer:", integer_value, type(integer_value))
print("Float:", float_value, type(float_value))
print("Complex:", complex_value, type(complex_value))

print("Addition:", integer_value + float_value)
print("Power:", integer_value ** 2)
print("Complex real part:", complex_value.real)
print("Complex imaginary part:", complex_value.imag)
