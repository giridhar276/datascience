"""Tuple syntax and unpacking."""

server = ("app-server-01", "Linux", 16)
name, operating_system, memory_gb = server

print("Tuple:", server)
print("Server name:", name)
print("Operating system:", operating_system)
print("Memory in GB:", memory_gb)

single_item_tuple = (100,)
print("Single-item tuple:", single_item_tuple)
