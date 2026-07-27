data = bytes([65, 66, 67, 68])

with open("sample.bin", "wb") as file:
    file.write(data)

with open("sample.bin", "rb") as file:
    print(file.read())
