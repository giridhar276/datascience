class Device:
    def power_on(self):
        return "Device powered on"

class Computer(Device):
    def compute(self):
        return "Computer is processing"

class Laptop(Computer):
    def portable(self):
        return "Laptop is portable"

class Desktop(Computer):
    def upgrade(self):
        return "Desktop is easy to upgrade"

laptop = Laptop()
desktop = Desktop()
print(laptop.power_on(), laptop.compute(), laptop.portable())
print(desktop.power_on(), desktop.compute(), desktop.upgrade())
