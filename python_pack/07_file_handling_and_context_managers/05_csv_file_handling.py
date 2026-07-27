import csv

rows = [
    ["employee_id", "name", "score"],
    [101, "Anita", 88],
    [102, "Ravi", 91],
]

with open("scores.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("scores.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
