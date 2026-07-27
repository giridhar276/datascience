class Employee:
    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department

    def display(self):
        print(self.employee_id, self.name, self.department)

employee = Employee(101, "Anita", "Analytics")
employee.display()
