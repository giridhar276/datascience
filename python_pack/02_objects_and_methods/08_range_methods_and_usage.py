"""Range object methods and properties."""

values = range(2, 12, 2)
print("Range as list:", list(values))
print("start:", values.start)
print("stop:", values.stop)
print("step:", values.step)
print("count of 6:", values.count(6))
print("index of 8:", values.index(8))
print("membership:", 10 in values)
