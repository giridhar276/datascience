company = "Global Tech"

def outer():
    department = "Analytics"

    def inner():
        nonlocal department
        department = "AI Analytics"
        local_value = "Local to inner"
        print(local_value)

    inner()
    print("Nonlocal value:", department)


def change_company():
    global company
    company = "Global AI Tech"

outer()
change_company()
print("Global value:", company)
