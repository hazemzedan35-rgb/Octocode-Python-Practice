correct_password = 'r4Hw123'
user_input = input("your password: ")
while user_input != correct_password:
    print("you enter a wrong password")
    user_input = input("please enter your password again")
print("welcome back")