import re

phone_number = input("what is ur phone number? ").strip()

if re.search(r"^\d{3}-\d{3}-\d{4}$", phone_number):
    print("valid")

else:
    print("invalid")
