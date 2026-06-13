correct_number = "5"
entering_number = input("guess a number from 1:10\n")
while entering_number != correct_number:
    if int(entering_number) >= 6:
        print("too high")
    elif int(entering_number) < 5:
        print("too low")
    entering_number = input("please try again\n")
print("congratilations! your guessing is true")

