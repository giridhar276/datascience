class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()

    def drive(self):
        return f"{self.model}: {self.engine.start()} and car is moving"

car = Car("Model X")
print(car.drive())
