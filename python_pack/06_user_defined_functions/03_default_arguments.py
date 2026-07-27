def create_profile(name, role="Learner", active=True):
    return {"name": name, "role": role, "active": active}

print(create_profile("Anita"))
print(create_profile("Ravi", "Trainer"))
print(create_profile("Meera", active=False))
