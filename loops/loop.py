# def main():
#     number = get_number()
#     meow(number)


# def get_number():
#     while True:
#         n = int(input("what is n: "))
#         if n > 0 and n <= 10:
#             break
#     return n 

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

# # def main():
# #     if "STEM2026" == get_password():
# #         print("Access Granted")


# # def get_password():
# #     while True:
# #         correct_pass = input("enter your password: ")
# #         if correct_pass == "STEM2026":
# #             break
# #     return correct_pass

# # main()
def main():
    print_hash(3)

def print_hash(size):
    for i in size:
        for j in size:
            print("#", end=(""))
        print()
main()