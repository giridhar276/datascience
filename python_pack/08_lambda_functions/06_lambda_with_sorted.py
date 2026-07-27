employees = [
    {"name": "Ravi", "score": 82},
    {"name": "Anita", "score": 94},
    {"name": "Meera", "score": 88},
]

by_score = sorted(employees, key=lambda employee: employee["score"], reverse=True)
by_name = sorted(employees, key=lambda employee: employee["name"])

print(by_score)
print(by_name)
