"""Bytes and bytearray objects."""

text = "Python"
encoded = text.encode("utf-8")
print("Encoded bytes:", encoded)
print("Decoded text:", encoded.decode("utf-8"))
print("bytes count:", encoded.count(b"t"))
print("bytes find:", encoded.find(b"th"))
print("bytes replace:", encoded.replace(b"Py", b"Jython"))

mutable_data = bytearray(b"ABC")
mutable_data.append(68)
mutable_data.extend(b"EF")
mutable_data.reverse()
print("bytearray after operations:", mutable_data)
