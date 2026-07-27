"""Common dictionary methods."""

employee = {"id": 101, "name": "Meera", "department": "IT"}

print("keys:", employee.keys())
print("values:", employee.values())
print("items:", employee.items())
print("get existing:", employee.get("name"))
print("get missing with default:", employee.get("salary", 0))

employee.update({"location": "Bengaluru", "department": "Cloud"})
print("update:", employee)

print("setdefault existing:", employee.setdefault("name", "Unknown"))
print("setdefault missing:", employee.setdefault("status", "Active"))

removed = employee.pop("location")
print("pop value:", removed, employee)

last_pair = employee.popitem()
print("popitem:", last_pair, employee)

copied = employee.copy()
print("copy:", copied)

new_dict = dict.fromkeys(["Python", "SQL", "Cloud"], "Pending")
print("fromkeys:", new_dict)

copied.clear()
print("clear:", copied)
