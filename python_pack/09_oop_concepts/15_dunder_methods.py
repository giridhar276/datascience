class Batch:
    def __init__(self, name, participants):
        self.name = name
        self.participants = participants

    def __len__(self):
        return len(self.participants)

    def __str__(self):
        return f"Batch {self.name} with {len(self)} participants"

    def __getitem__(self, index):
        return self.participants[index]

batch = Batch("July", ["Anita", "Ravi", "Meera"])
print(batch)
print(len(batch))
print(batch[0])
