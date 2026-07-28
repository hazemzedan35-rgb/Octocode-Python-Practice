import re

name = input("what is your first and last name? ").strip()

if re.search(r"^[a-zA-Z]{2,} [a-zA-Z]{2,}$", name):
    print("valid")

else:
    print("invalid")