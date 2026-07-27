"""Creating, reading and updating lists."""

technologies = ["Python", "SQL", "Pandas", "Flask"]
print("Original list:", technologies)
print("First item:", technologies[0])
print("Last two items:", technologies[-2:])

technologies[1] = "MySQL"
technologies.append("FastAPI")
print("Updated list:", technologies)
