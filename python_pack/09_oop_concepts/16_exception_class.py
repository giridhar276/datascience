class InsufficientBalanceError(Exception):
    """Raised when a withdrawal is larger than the available balance."""

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.balance -= amount
        return self.balance

account = Account(1000)
try:
    print(account.withdraw(1200))
except InsufficientBalanceError as error:
    print(error)
