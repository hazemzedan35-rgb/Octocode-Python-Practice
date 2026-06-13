countries = input("please input some countries: ").split(", ")
for x in countries:
    print(x)
    response = input("did you visit this country befor? (yes, no)").strip().lower()
    if response == "yes":
        print("i hope you spent good day")
    else:
        print("I hope you get to visit it soon")
    print("---------")
