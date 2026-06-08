x = input ("""What do you need help with?
1. Study
2. English
3. Programming
4. Mental Health\n""").lower()
if x == "study" or x == "1":
    study_time = int(input ("How many hours do you study per one day?"))
    if study_time < 2:
        print("you need to study more")
    elif 2 <= study_time <= 4:
        print("you are a good student")
    elif study_time > 4:
        print("you have an excellent discipline")
elif x == "english" or x == "2":
    speaking_test= input("Do you practice speaking every day?").lower().strip()
    if speaking_test == "yes":
        print("keep going you are in the right road")
    elif speaking_test == "no":
        print("practice shadowing for 10 minutes every day and you will be good")
elif x == "programming" or x == "3":
    cs50p_session = input("Did you finish conditionals session?").lower().strip()
    if cs50p_session == 'yes':
        print("ohh yeah! go and solve the problem set")
    elif cs50p_session == 'no':
        print("finish the session first then go and solve the problem set")
elif x== "mental health" or x == "4":
    comparing = input("Do you compare yourself to others a lot?").lower().strip()
    if comparing == 'yes':
        print("you need to focus on yourself, focus on your goals, focus on knowing yourself")
    elif comparing == 'no':
        print("keep going!!")
else:
    print("please choose from the 4 options!!")

