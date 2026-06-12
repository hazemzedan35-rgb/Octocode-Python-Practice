weight = int(input("what is your weight?").strip())
workout_days = int(input("how many days do you go to the gym?").strip())
protein = int(input("how many grams of protein do you eat each day?").strip())
def excercise():
    if workout_days < 3:
       return "play more days"
    elif  3 <= workout_days <= 5:
       return"you go for enough days to the gym"
    elif workout_days > 5:
        return "Rest a bit for recovery"
def value_protein():
    main = 2 * weight
    if protein < main:
        return f"you need to eat {main} of proteins"
    elif protein <= main:
        return "your protein value is good"
print(excercise())
print(value_protein())