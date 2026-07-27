file_name = "pointer_demo.txt"
with open(file_name, "w+", encoding="utf-8") as file:
    file.write("ABCDEFGHIJ")
    print("Pointer after write:", file.tell())
    file.seek(0)
    print("First four characters:", file.read(4))
    print("Pointer after read:", file.tell())
