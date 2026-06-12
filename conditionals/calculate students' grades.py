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

