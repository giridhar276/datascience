"""Useful methods and attributes of int, float and complex objects."""

number = 25
print("bit_length:", number.bit_length())
print("bit_count:", number.bit_count())
print("to_bytes:", number.to_bytes(2, byteorder="big"))
print("from_bytes:", int.from_bytes(b"\x00\x19", byteorder="big"))
print("as_integer_ratio:", number.as_integer_ratio())

price = 19.75
print("float as_integer_ratio:", price.as_integer_ratio())
print("is_integer:", price.is_integer())
print("hex:", price.hex())
print("fromhex:", float.fromhex(price.hex()))

value = 3 + 4j
print("real:", value.real)
print("imag:", value.imag)
print("conjugate:", value.conjugate())
