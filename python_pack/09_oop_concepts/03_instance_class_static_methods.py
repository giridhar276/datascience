class Training:
    organization = "Tech Academy"

    def __init__(self, topic):
        self.topic = topic

    def instance_method(self):
        return f"Topic: {self.topic}"

    @classmethod
    def class_method(cls):
        return f"Organization: {cls.organization}"

    @staticmethod
    def static_method(hours):
        return hours > 0

training = Training("Python")
print(training.instance_method())
print(Training.class_method())
print(Training.static_method(4))
