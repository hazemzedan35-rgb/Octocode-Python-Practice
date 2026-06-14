print("***welcome to Multiplication Table***")
number = int(input("enter your number: "))


for x in range(1, 11):
    result = x * number
    print(f"{number} * {x} = {result}")