names = ["Asha", "Bala", "Charan"]
scores = [82, 76, 91]

for position, name in enumerate(names, start=1):
    print(position, name)

for name, score in zip(names, scores):
    print(f"{name}: {score}")
