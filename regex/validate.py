import re

email = input("what's your email? ").strip().lower()

if re.search(r"^\w+@\w+\.edu$", email):
    print("valid")
else:
    print("invalid")


 