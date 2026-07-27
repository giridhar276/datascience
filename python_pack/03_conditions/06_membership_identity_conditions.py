roles = ["admin", "trainer", "learner"]
selected_role = "trainer"

if selected_role in roles:
    print("Valid role")

first = [1, 2]
second = first
if first is second:
    print("Both variables refer to the same object")
