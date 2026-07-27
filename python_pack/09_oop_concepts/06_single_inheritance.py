class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}"

class Trainer(Person):
    def teach(self):
        return f"{self.name} is teaching Python"

trainer = Trainer("Giridhar")
print(trainer.introduce())
print(trainer.teach())
