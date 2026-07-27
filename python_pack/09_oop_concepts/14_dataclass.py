from dataclasses import dataclass

@dataclass
class Course:
    name: str
    duration_hours: int
    active: bool = True

course = Course("Python Fundamentals", 24)
print(course)
print(course.name)
