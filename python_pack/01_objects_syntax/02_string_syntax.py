"""Creating and accessing strings."""

single_quoted = 'Python'
double_quoted = "Programming"
multiline = """Python is easy to learn.
It is widely used in automation, analytics and AI."""

message = single_quoted + " " + double_quoted
print(message)
print("First character:", message[0])
print("Last character:", message[-1])
print("Slice:", message[0:6])
print(multiline)
