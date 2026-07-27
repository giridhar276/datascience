"""Common set methods and set relationships."""

first = {1, 2, 3, 4}
second = {3, 4, 5, 6}

sample = first.copy()
sample.add(7)
print("add:", sample)

sample.update({8, 9})
print("update:", sample)

sample.remove(9)
print("remove:", sample)

sample.discard(100)  # No error when item is absent.
print("discard absent item:", sample)

removed = sample.pop()
print("pop:", removed, sample)

print("union:", first.union(second))
print("intersection:", first.intersection(second))
print("difference:", first.difference(second))
print("symmetric_difference:", first.symmetric_difference(second))
print("isdisjoint:", first.isdisjoint({10, 11}))
print("issubset:", {1, 2}.issubset(first))
print("issuperset:", first.issuperset({1, 2}))

sample.intersection_update(second)
print("intersection_update:", sample)
sample.clear()
print("clear:", sample)
