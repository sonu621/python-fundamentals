# ----------------- Match Case in Python --------------------

# match-case was introduced in Python 3.10.
# It is used for pattern matching (similar to switch-case in other languages, but more powerful).

# For example:-
'''def check_status(status):
    match status:
        case "active":
            return "User is active"
        case "inactive":
            return "User is inactive"
        case _:
            return "Unknown status"

print(check_status("active"))'''


'''def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
          return  "Unknow Status"

print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(5001))'''