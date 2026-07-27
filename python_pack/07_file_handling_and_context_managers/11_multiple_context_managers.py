with open("source.txt", "w", encoding="utf-8") as source:
    source.write("Python context managers simplify resource handling.")

with open("source.txt", "r", encoding="utf-8") as source, \
     open("destination.txt", "w", encoding="utf-8") as destination:
    destination.write(source.read())

print("File copied successfully")
