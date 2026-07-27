class Employee:
    company = "ABC Technologies"

    def work(self):
        return "Working"

employee = Employee()
print("callable method:", callable(employee.work))
print("hasattr company:", hasattr(employee, "company"))
print("getattr company:", getattr(employee, "company"))
setattr(employee, "location", "Hyderabad")
print("new attribute:", employee.location)
delattr(employee, "location")
print("attribute removed:", not hasattr(employee, "location"))
print("dir sample:", [name for name in dir(employee) if not name.startswith("__")])
