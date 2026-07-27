file_name = "training_log.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("Session 1 completed\n")

with open(file_name, "a", encoding="utf-8") as file:
    file.write("Session 2 completed\n")

with open(file_name, "r", encoding="utf-8") as file:
    print(file.read())
