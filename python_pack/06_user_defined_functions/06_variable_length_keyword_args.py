def create_record(**details):
    print("Received dictionary:", details)
    for key, value in details.items():
        print(f"{key}: {value}")

create_record(name="Ravi", role="Developer", location="Pune")
