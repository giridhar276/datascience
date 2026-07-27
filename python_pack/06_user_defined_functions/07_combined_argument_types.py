def register(name, department="General", *skills, **metadata):
    print("Name:", name)
    print("Department:", department)
    print("Skills:", skills)
    print("Metadata:", metadata)

register("Anita", "AI", "Python", "ML", experience=5, location="Hyderabad")
