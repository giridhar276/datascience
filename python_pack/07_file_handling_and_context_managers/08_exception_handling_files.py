try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError as error:
    print("File not found:", error)
except PermissionError as error:
    print("Permission denied:", error)
else:
    print("File processed successfully")
finally:
    print("File operation finished")
