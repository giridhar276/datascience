class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # Public
        self._account_type = "Savings"  # Protected by convention
        self.__balance = balance         # Name-mangled private attribute

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Ravi", 1000)
account.deposit(500)
print(account.owner)
print(account._account_type)
print(account.get_balance())
