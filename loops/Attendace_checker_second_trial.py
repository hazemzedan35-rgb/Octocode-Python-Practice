Attendees = input("Enter the names of attendees and separted them by comma").strip().lower().split(", ")
for person in Attendees:
    print(person)
    x = input("is this person attending? ").strip().lower()
    if x == "no":
        print("Attendance not confermed")
    else:
        print("Attendance confermed")
    print("-----")

