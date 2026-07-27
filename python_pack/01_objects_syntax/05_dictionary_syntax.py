"""Dictionary syntax using key-value pairs."""

employee = {
    "id": 101,
    "name": "Anita",
    "department": "Analytics",
    "active": True,
}

print(employee)
print("Name:", employee["name"])
print("Department:", employee.get("department"))

employee["location"] = "Hyderabad"
employee["active"] = False
print("Updated dictionary:", employee)
