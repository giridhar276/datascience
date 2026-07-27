class ManagedFile:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file")
        self.file = open(self.file_name, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file")
        if self.file:
            self.file.close()
        return False

with ManagedFile("managed.txt", "w") as file:
    file.write("Created using a custom context manager")
