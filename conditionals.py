# application check the suitable age for using the app
print("welcome to my app.")
age = int(input("how old are you?\n"))
if age >= 12:
    print("you can use app!")
else:
    print("sorry you can't use the app")
    print("you are so young!!!")
#this is a new app that determines the sign of any number
number = float(input("please, input the number\n"))
if number > 0:
    print("the number is positive!") 
elif number < 0:
    print("the number is negative!")
else:
    print("the number is zero!")
#this is the app that calculate the grade of students 
degree = float(input("what is your degree?\n"))
if degree >= 90:
    print("you got A grade!")
elif degree >= 75:
    print("you got B grade!")
elif degree >= 50:
    print("you got C grade!")
else:
    print("you got f grade!")
# another program that check the number of chair that win or lose a discount 
seat_number = int(input("what is you chair number?"))
if seat_number != 13:
    print("you win a discount")
else:
    print("sorry! you lose the discount")
# application checks user password
password = input("what is you password\n")
if password == "abc":
    print("welcome!")
else:
    print("password is wrong!!")
# application tell the user what word he wrote
word = input("write a word from these(yes, no, maybe)\n")
if word == "yes":
    print("you wrote \"yes\"")
elif word == "no":
    print("you wrote \"no\"")
else:
    print("you wrote\"maybe\"")
# application that check a write number 
number = input("guess a number")
if number != 7:
    print("sorry the number is wrong!!!")
else:
    print("wow!you write the correct number")