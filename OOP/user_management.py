class User:
    def __init__(self, first_name, last_name, email, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.status = status

    def __str__(self):
        return f"""First Name: {self.first_name}
Last Name: {self.last_name}
Email: {self.email}
Status: {self.status}
---------------------------"""

users = []

def main():
    while True:
        action = get_action()
        if action == "1":
            get_user_information()
            continue
        elif action == "2":
            for i in users:
                print(i)
                continue
        elif action == "3":
            break



def get_action():
    choice = input("""Choose an action:\n
    1. Add new user
    2. Display all users
    3. Exit\n""")

    return choice

        
def get_user_information():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")

    user = User(first_name, last_name, email)
    users.append(user)
    return user



if __name__=="__main__":
    main()