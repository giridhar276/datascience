class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

employees = [Employee("Anita"), Employee("Ravi")]
department = Department("Analytics", employees)
print(department.name)
print([employee.name for employee in department.employees])
