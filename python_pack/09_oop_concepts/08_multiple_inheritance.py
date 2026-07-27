class Camera:
    def capture(self):
        return "Photo captured"

class GPS:
    def locate(self):
        return "Location identified"

class Smartphone(Camera, GPS):
    def call(self):
        return "Calling"

phone = Smartphone()
print(phone.capture())
print(phone.locate())
print(phone.call())
print("MRO:", [cls.__name__ for cls in Smartphone.mro()])
