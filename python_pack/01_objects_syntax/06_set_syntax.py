"""Set syntax and uniqueness."""

skills = {"Python", "SQL", "Python", "Git"}
print("Unique skills:", skills)

skills.add("Docker")
skills.discard("Git")
print("Updated set:", skills)

required = {"Python", "SQL", "Cloud"}
print("Common skills:", skills & required)
print("All skills:", skills | required)
