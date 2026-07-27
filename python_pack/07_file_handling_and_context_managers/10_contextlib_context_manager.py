from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    resource = {"name": name, "status": "ready"}
    try:
        yield resource
    finally:
        resource["status"] = "closed"
        print(f"Released {name}")

with managed_resource("database connection") as connection:
    print(connection)
