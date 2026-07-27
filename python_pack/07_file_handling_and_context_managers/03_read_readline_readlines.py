file_name = "participants.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Anita\nRavi\nMeera\n")

with open(file_name, "r", encoding="utf-8") as file:
    print("readline:", file.readline().strip())
    print("remaining readlines:", [line.strip() for line in file.readlines()])
