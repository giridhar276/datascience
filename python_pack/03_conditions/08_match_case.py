"""Requires Python 3.10 or later."""

status_code = 404
match status_code:
    case 200:
        print("Success")
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case _:
        print("Unknown status")
