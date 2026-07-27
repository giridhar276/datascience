from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using card"

class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using UPI"

for payment in [CardPayment(), UPIPayment()]:
    print(payment.pay(500))
